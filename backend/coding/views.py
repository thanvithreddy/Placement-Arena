from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import CodingProblem, SampleTestCase, HiddenTestCase, CodingSubmission
from .serializers import CodingProblemSerializer, CodingSubmissionSerializer, AdminCodingProblemSerializer, SampleTestCaseSerializer, HiddenTestCaseSerializer
from .piston import execute_code
from exams.models import ExamAttempt, SectionAttempt
from django.utils import timezone
import math


class CodingProblemsListView(APIView):
    """List coding problems, optionally filtered by section_id."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        section_id = request.query_params.get('section_id')
        if section_id:
            problems = CodingProblem.objects.filter(section_id=section_id).order_by('order')
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
        
        passed_sample = 0
        for case in problem.sample_cases.all():
            res = execute_code(language, code, case.input_data, timeout=timeout)
            if res['status'] == 'ok' and res['stdout'].strip() == case.expected_output.strip():
                passed_sample += 1
                
        passed_hidden = 0
        total_weight = 0
        passed_weight = 0
        
        for case in problem.hidden_cases.all():
            total_weight += case.score_weight
            res = execute_code(language, code, case.input_data, timeout=timeout)
            if res['status'] == 'ok' and res['stdout'].strip() == case.expected_output.strip():
                passed_hidden += 1
                passed_weight += case.score_weight
                
        score = (passed_weight / total_weight * problem.max_score) if total_weight > 0 else 0
        
        overall_status = 'accepted' if passed_hidden == problem.hidden_cases.count() else 'wrong_answer'
        
        submission = CodingSubmission.objects.create(
            user=request.user,
            exam_attempt=attempt,
            problem=problem,
            language=language,
            code=code,
            status=overall_status,
            score=score,
            passed_sample=passed_sample,
            total_sample=problem.sample_cases.count(),
            passed_hidden=passed_hidden,
            total_hidden=problem.hidden_cases.count(),
            is_final=True
        )
        
        if attempt:
            # Update the coding section attempt score.
            # Find by section_type='coding' since problem.section may be None.
            try:
                section_attempt = SectionAttempt.objects.get(
                    exam_attempt=attempt,
                    section__section_type='coding'
                )
                section_attempt.score = min(
                    section_attempt.score + score,
                    section_attempt.section.max_score
                )
                section_attempt.save()

                # Recalculate total score from all section scores
                attempt.total_score = sum(
                    sa.score for sa in attempt.section_attempts.all()
                )
                attempt.save()
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
        problems = CodingProblem.objects.all().order_by('-id')
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

