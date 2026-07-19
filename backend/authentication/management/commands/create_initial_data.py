from django.core.management.base import BaseCommand
from authentication.models import User
from exams.models import Exam, ExamSection
from questions.models import Question, Option
from coding.models import CodingProblem, SampleTestCase, HiddenTestCase
from datetime import date

class Command(BaseCommand):
    help = 'Create initial data for Placement Arena'

    def handle(self, *args, **kwargs):
        # 1. Create Users
        admin, _ = User.objects.get_or_create(username='admin1', defaults={'role': 'admin', 'display_name': 'Admin User'})
        if _: admin.set_password('admin@123'); admin.save()
        
        c1, _ = User.objects.get_or_create(username='candidate1', defaults={'role': 'candidate', 'display_name': 'Candidate One'})
        if _: c1.set_password('candidate@123'); c1.save()
        
        c2, _ = User.objects.get_or_create(username='candidate2', defaults={'role': 'candidate', 'display_name': 'Candidate Two'})
        if _: c2.set_password('candidate@123'); c2.save()

        self.stdout.write('Created users')

        # 2. Create Exam
        exam, created = Exam.objects.get_or_create(
            title='Placement Mock Test 1',
            defaults={
                'date': date.today(),
                'status': 'active',
                'created_by': admin,
                'description': 'A comprehensive mock test for campus placements.'
            }
        )

        if created:
            sec1 = ExamSection.objects.create(exam=exam, section_type='arithmetic', order=1, duration_minutes=20, max_score=100, question_count=25)
            sec2 = ExamSection.objects.create(exam=exam, section_type='verbal', order=2, duration_minutes=20, max_score=80, question_count=20)
            sec3 = ExamSection.objects.create(exam=exam, section_type='reasoning', order=3, duration_minutes=20, max_score=100, question_count=25)
            sec4 = ExamSection.objects.create(exam=exam, section_type='coding', order=4, duration_minutes=60, max_score=200, question_count=2)
            
            # 3. Create Questions for Arithmetic
            q_data = [
                ("What is 15% of 200?", "30", ["20", "30", "40", "50"]),
                ("If a train 100m long passes a pole in 10s, what is its speed in m/s?", "10", ["5", "10", "15", "20"]),
                ("Solve for x: 2x + 5 = 15", "5", ["3", "4", "5", "6"]),
                ("A pipe fills a tank in 2 hours, another in 3 hours. Together?", "1.2 hours", ["1 hour", "1.2 hours", "1.5 hours", "5 hours"]),
                ("What is the square root of 144?", "12", ["10", "12", "14", "16"]),
            ]
            
            for i, (text, correct_ans, options) in enumerate(q_data):
                q = Question.objects.create(section=sec1, category='arithmetic', difficulty='easy', text=text, marks=4.0, order=i+1)
                for j, opt in enumerate(options):
                    Option.objects.create(question=q, text=opt, is_correct=(opt==correct_ans), order=j+1)
                    
            # 4. Create Coding Problems
            p1 = CodingProblem.objects.create(
                section=sec4, title='Reverse String', statement='Write a function to reverse a string.',
                input_format='A single string S', output_format='Reversed string S',
                difficulty='easy', max_score=100, order=1
            )
            SampleTestCase.objects.create(problem=p1, input_data='hello', expected_output='olleh', order=1)
            SampleTestCase.objects.create(problem=p1, input_data='world', expected_output='dlrow', order=2)
            HiddenTestCase.objects.create(problem=p1, input_data='placement', expected_output='tnemecalp', score_weight=1.0, order=1)
            HiddenTestCase.objects.create(problem=p1, input_data='arena', expected_output='anera', score_weight=1.0, order=2)
            HiddenTestCase.objects.create(problem=p1, input_data='python', expected_output='nohtyp', score_weight=1.0, order=3)
            
            p2 = CodingProblem.objects.create(
                section=sec4, title='Two Sum', statement='Find two numbers that add up to target.',
                input_format='N integers followed by target', output_format='Indices (0-based) separated by space',
                difficulty='medium', max_score=100, order=2
            )
            SampleTestCase.objects.create(problem=p2, input_data='2 7 11 15\n9', expected_output='0 1', order=1)
            SampleTestCase.objects.create(problem=p2, input_data='3 2 4\n6', expected_output='1 2', order=2)
            HiddenTestCase.objects.create(problem=p2, input_data='3 3\n6', expected_output='0 1', score_weight=1.0, order=1)
            HiddenTestCase.objects.create(problem=p2, input_data='1 2 3 4 5\n9', expected_output='3 4', score_weight=1.0, order=2)
            HiddenTestCase.objects.create(problem=p2, input_data='0 4 3 0\n0', expected_output='0 3', score_weight=1.0, order=3)

            self.stdout.write('Created exam, questions, and coding problems')
        else:
            self.stdout.write('Exam already exists')

        # Add Verbal + Reasoning free questions if not exist
        if Question.objects.filter(category='verbal').count() == 0:
            verbal_q_data = [
                ("Choose the correct sentence: options are 4 sentences, one grammatically correct", "One grammatically correct sentence", ["Sentence 1", "Sentence 2", "One grammatically correct sentence", "Sentence 4"]),
                ("Antonym of 'Benevolent'", "Malevolent", ["Malevolent", "Generous", "Kind", "Helpful"]),
                ("Fill in the blank: 'She __ the report yesterday.'", "submitted", ["submitted", "submits", "will submit", "submitting"]),
                ("Synonym of 'Ephemeral'", "Fleeting", ["Eternal", "Fleeting", "Permanent", "Lasting"]),
                ("Correct the error: 'He don't know the answer'", "He doesn't know the answer", ["He do not know", "He doesn't know the answer", "He hasn't know", "He didn't knew"])
            ]
            for i, (text, correct_ans, options) in enumerate(verbal_q_data):
                q = Question.objects.create(section=None, category='verbal', difficulty='medium', text=text, marks=4.0, order=i+1)
                for j, opt in enumerate(options):
                    Option.objects.create(question=q, text=opt, is_correct=(opt==correct_ans), order=j+1)
                    
            reasoning_q_data = [
                ("Number series: 2, 4, 8, 16, _?", "32", ["32", "24", "28", "20"]),
                ("If A is B's sister, B is C's brother, what is A to C?", "Sister", ["Sister", "Brother", "Mother", "Aunt"]),
                ("Which is odd one out?", "Bat", ["Eagle", "Sparrow", "Bat", "Pigeon"]),
                ("Mirror Image: PAINT → what does it look like in mirror?", "TNIAP", ["TNIAP", "TNIPD", "TNIAP", "TNIAD"]),
                ("If 'MANGO' = 51, 'APPLE' = 50, then 'GRAPE' = ?", "52", ["49", "52", "47", "45"])
            ]
            for i, (text, correct_ans, options) in enumerate(reasoning_q_data):
                q = Question.objects.create(section=None, category='reasoning', difficulty='medium', text=text, marks=4.0, order=i+1)
                for j, opt in enumerate(options):
                    Option.objects.create(question=q, text=opt, is_correct=(opt==correct_ans), order=j+1)
            
            self.stdout.write('Created seed Verbal and Reasoning questions')
