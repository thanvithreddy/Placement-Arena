from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import CodingProblem, SampleTestCase, HiddenTestCase, CodingSubmission
from .serializers import CodingProblemSerializer, CodingSubmissionSerializer, AdminCodingProblemSerializer, SampleTestCaseSerializer, HiddenTestCaseSerializer
from .piston import execute_code
from exams.models import ExamAttempt, SectionAttempt
from django.utils import timezone
import math
import openpyxl
import csv
import io


class CodingProblemsListView(APIView):
    """List coding problems, optionally filtered by section_id."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        section_id = request.query_params.get('section_id')
        if section_id:
            problems = CodingProblem.objects.filter(section_id=section_id).order_by('order')
            if not problems.exists():
                problems = CodingProblem.objects.all().order_by('order')
        else:
            problems = CodingProblem.objects.all().order_by('order')
        return Response(CodingProblemSerializer(problems, many=True).data)

class CodingProblemView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            problem = CodingProblem.objects.get(id=id)
            return Response(CodingProblemSerializer(problem).data)
        except CodingProblem.DoesNotExist:
            return Response({'error': 'Problem not found'}, status=status.HTTP_404_NOT_FOUND)

class RunCodeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        problem_id = request.data.get('problem_id')
        language = request.data.get('language')
        code = request.data.get('code')
        custom_input = request.data.get('custom_input')
        
        try:
            problem = CodingProblem.objects.get(id=problem_id)
        except CodingProblem.DoesNotExist:
            return Response({'error': 'Problem not found'}, status=status.HTTP_404_NOT_FOUND)
            
        timeout = math.ceil(problem.time_limit_ms / 1000)
        
        if custom_input is not None:
            result = execute_code(language, code, custom_input, timeout=timeout)
            return Response({'custom_run': result})
            
        # Run against sample cases
        results = []
        passed = 0
        for case in problem.sample_cases.all():
            res = execute_code(language, code, case.input_data, timeout=timeout)
            expected = case.expected_output.strip()
            actual = res['stdout'].strip()
            
            is_correct = False
            if res['status'] == 'ok' and actual == expected:
                is_correct = True
                passed += 1
                
            results.append({
                'case_id': case.id,
                'input': case.input_data,
                'expected': expected,
                'actual': actual,
                'stderr': res['stderr'],
                'status': res['status'],
                'is_correct': is_correct
            })
            
        return Response({
            'passed': passed,
            'total': problem.sample_cases.count(),
            'results': results
        })

class SubmitCodeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        problem_id = request.data.get('problem_id')
        language = request.data.get('language')
        code = request.data.get('code')
        exam_attempt_id = request.data.get('exam_attempt_id')
        
        try:
            problem = CodingProblem.objects.get(id=problem_id)
            attempt = ExamAttempt.objects.get(id=exam_attempt_id, user=request.user) if exam_attempt_id else None
        except (CodingProblem.DoesNotExist, ExamAttempt.DoesNotExist):
            return Response({'error': 'Invalid problem or attempt'}, status=status.HTTP_400_BAD_REQUEST)
            
        timeout = math.ceil(problem.time_limit_ms / 1000)
        
        # Test against sample cases
        passed_sample = 0
        for case in problem.sample_cases.all():
            res = execute_code(language, code, case.input_data, timeout=timeout)
            if res['status'] == 'ok' and res['stdout'].strip() == case.expected_output.strip():
                passed_sample += 1
                
        # Test against hidden cases
        passed_hidden = 0
        total_hidden_weight = 0
        earned_hidden_weight = 0
        for case in problem.hidden_cases.all():
            total_hidden_weight += case.score_weight
            res = execute_code(language, code, case.input_data, timeout=timeout)
            if res['status'] == 'ok' and res['stdout'].strip() == case.expected_output.strip():
                passed_hidden += 1
                earned_hidden_weight += case.score_weight
                
        # Calculate proportional score based on hidden test cases
        if total_hidden_weight > 0:
            score = (earned_hidden_weight / total_hidden_weight) * problem.max_score
        else:
            total_samples = problem.sample_cases.count()
            score = (passed_sample / total_samples * problem.max_score) if total_samples > 0 else 0
            
        submission = CodingSubmission.objects.create(
            user=request.user,
            exam_attempt=attempt,
            problem=problem,
            language=language,
            code=code,
            status='accepted' if (passed_hidden == problem.hidden_cases.count() and passed_sample == problem.sample_cases.count()) else 'wrong_answer',
            score=score,
            passed_sample=passed_sample,
            total_sample=problem.sample_cases.count(),
            passed_hidden=passed_hidden,
            total_hidden=problem.hidden_cases.count(),
            is_final=True
        )
        
        # Update SectionAttempt and ExamAttempt scores
        if attempt:
            try:
                coding_section_attempt = SectionAttempt.objects.get(
                    exam_attempt=attempt,
                    section__section_type='coding'
                )
                
                # Get max score across all coding submissions for this attempt
                all_coding_scores = CodingSubmission.objects.filter(
                    exam_attempt=attempt,
                    is_final=True
                ).values('problem').annotate(
                    max_prob_score=models.Max('score')
                )
                
                total_coding_score = sum(item['max_prob_score'] for item in all_coding_scores)
                coding_section_attempt.score = total_coding_score
                coding_section_attempt.save()
                
            except SectionAttempt.DoesNotExist:
                pass
                
        return Response(CodingSubmissionSerializer(submission).data)

class CodingHistoryView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, problem_id):
        submissions = CodingSubmission.objects.filter(
            user=request.user,
            problem_id=problem_id
        ).order_by('-submitted_at')
        return Response(CodingSubmissionSerializer(submissions, many=True).data)

class AdminCodingProblemView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        problems = CodingProblem.objects.all()
        return Response(AdminCodingProblemSerializer(problems, many=True).data)

    def post(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        serializer = AdminCodingProblemSerializer(data=request.data)
        if serializer.is_valid():
            section = serializer.validated_data.get('section')
            if not section:
                from exams.models import ExamSection
                section = ExamSection.objects.filter(section_type='coding').last()
            serializer.save(section=section)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminCodingProblemDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        try:
            problem = CodingProblem.objects.get(id=id)
            return Response(AdminCodingProblemSerializer(problem).data)
        except CodingProblem.DoesNotExist:
            return Response({'error': 'Problem not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        try:
            problem = CodingProblem.objects.get(id=id)
            problem.delete()
            return Response({'message': 'Problem deleted successfully'})
        except CodingProblem.DoesNotExist:
            return Response({'error': 'Problem not found'}, status=status.HTTP_404_NOT_FOUND)

class AdminTestCaseView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        try:
            problem = CodingProblem.objects.get(id=id)
        except CodingProblem.DoesNotExist:
            return Response({'error': 'Problem not found'}, status=status.HTTP_404_NOT_FOUND)
            
        case_type = request.data.get('type')
        if case_type == 'sample':
            serializer = SampleTestCaseSerializer(data=request.data)
        else:
            serializer = HiddenTestCaseSerializer(data=request.data)
            
        if serializer.is_valid():
            serializer.save(problem=problem)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BulkImportCodingView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
            
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
        filename = file_obj.name.lower()
        rows = []

        if filename.endswith('.csv') or 'csv' in file_obj.content_type:
            try:
                content = file_obj.read()
                try:
                    decoded = content.decode('utf-8-sig')
                except UnicodeDecodeError:
                    decoded = content.decode('latin-1')
                
                reader = csv.reader(io.StringIO(decoded))
                rows = list(reader)
            except Exception as e:
                return Response({'error': f'Failed to parse CSV file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                wb = openpyxl.load_workbook(file_obj, data_only=True)
                sheet = wb.active
                for r in sheet.iter_rows(values_only=True):
                    if r and any(cell is not None for cell in r):
                        rows.append([cell for cell in r])
            except Exception as e:
                return Response({'error': f'Failed to parse Excel file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
            
        if not rows:
            return Response({'error': 'Uploaded file is empty'}, status=status.HTTP_400_BAD_REQUEST)

        def clean_val(val):
            if val is None:
                return ""
            s = str(val).strip()
            s = s.replace('â‚¹', '₹').replace('â€™', "'").replace('â€"', "-")
            return s

        from exams.models import ExamSection
        default_section = ExamSection.objects.filter(section_type='coding').last()

        count = 0
        for idx, row in enumerate(rows):
            if not row:
                continue
                
            r = [clean_val(cell) for cell in row]
            title = r[0] if len(r) > 0 else ""

            # Skip header row if first cell matches title keywords
            if idx == 0 and title.lower() in ['title', 'problem_title', 'problem title', 'name', 'problem name']:
                continue

            if not title:
                continue

            diff = r[1].lower() if len(r) > 1 and r[1] else 'medium'
            if diff not in ['easy', 'medium', 'hard']:
                diff = 'medium'

            statement = r[2] if len(r) > 2 else ''
            input_format = r[3] if len(r) > 3 else ''
            output_format = r[4] if len(r) > 4 else ''

            sample_in_1 = r[5] if len(r) > 5 else ''
            sample_out_1 = r[6] if len(r) > 6 else ''
            sample_exp_1 = r[7] if len(r) > 7 else ''

            sample_in_2 = r[8] if len(r) > 8 else ''
            sample_out_2 = r[9] if len(r) > 9 else ''
            sample_exp_2 = r[10] if len(r) > 10 else ''

            hidden_in_1 = r[11] if len(r) > 11 else ''
            hidden_out_1 = r[12] if len(r) > 12 else ''

            hidden_in_2 = r[13] if len(r) > 13 else ''
            hidden_out_2 = r[14] if len(r) > 14 else ''

            hidden_in_3 = r[15] if len(r) > 15 else ''
            hidden_out_3 = r[16] if len(r) > 16 else ''

            try:
                max_score = int(float(r[17])) if len(r) > 17 and r[17] else 100
            except (ValueError, TypeError):
                max_score = 100

            try:
                time_limit = int(float(r[18])) if len(r) > 18 and r[18] else 5000
            except (ValueError, TypeError):
                time_limit = 5000

            problem = CodingProblem.objects.create(
                section=default_section,
                title=title,
                difficulty=diff,
                statement=statement or title,
                input_format=input_format,
                output_format=output_format,
                max_score=max_score,
                time_limit_ms=time_limit
            )

            # Sample test cases
            if sample_in_1 and sample_out_1:
                SampleTestCase.objects.create(problem=problem, input_data=sample_in_1, expected_output=sample_out_1, explanation=sample_exp_1, order=1)
            if sample_in_2 and sample_out_2:
                SampleTestCase.objects.create(problem=problem, input_data=sample_in_2, expected_output=sample_out_2, explanation=sample_exp_2, order=2)

            # Hidden test cases
            if hidden_in_1 and hidden_out_1:
                HiddenTestCase.objects.create(problem=problem, input_data=hidden_in_1, expected_output=hidden_out_1, score_weight=1.0, order=1)
            if hidden_in_2 and hidden_out_2:
                HiddenTestCase.objects.create(problem=problem, input_data=hidden_in_2, expected_output=hidden_out_2, score_weight=1.0, order=2)
            if hidden_in_3 and hidden_out_3:
                HiddenTestCase.objects.create(problem=problem, input_data=hidden_in_3, expected_output=hidden_out_3, score_weight=1.0, order=3)

            count += 1

        if count == 0:
            return Response({'error': 'No valid coding problems found in uploaded file. Please verify column layout.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': f'Successfully imported {count} coding problems with sample and hidden test cases!'})
