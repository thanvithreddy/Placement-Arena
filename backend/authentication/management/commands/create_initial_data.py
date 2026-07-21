from django.core.management.base import BaseCommand
from authentication.models import User
from exams.models import Exam, ExamSection, ExamAttempt, SectionAttempt
from questions.models import Question, Option, Answer
from coding.models import CodingProblem, SampleTestCase, HiddenTestCase, CodingSubmission
from warnings_log.models import ViolationLog
from leaderboard.models import DailyLeaderboard
from analytics.models import UserAnalytics

class Command(BaseCommand):
    help = 'Purge entire database and create ONLY Thanvith, Tejaswini, and admin1 accounts'

    def handle(self, *args, **kwargs):
        self.stdout.write('Wiping entire database...')
        
        # Purge all data
        ViolationLog.objects.all().delete()
        CodingSubmission.objects.all().delete()
        Answer.objects.all().delete()
        SectionAttempt.objects.all().delete()
        ExamAttempt.objects.all().delete()
        DailyLeaderboard.objects.all().delete()
        UserAnalytics.objects.all().delete()
        Option.objects.all().delete()
        Question.objects.all().delete()
        SampleTestCase.objects.all().delete()
        HiddenTestCase.objects.all().delete()
        CodingProblem.objects.all().delete()
        ExamSection.objects.all().delete()
        Exam.objects.all().delete()

        # Delete all users except admin1, Thanvith, Tejaswini
        User.objects.all().delete()

        # 1. Create Only Admin and 2 Candidates
        admin = User.objects.create(username='admin1', role='admin', display_name='Admin User', is_staff=True, is_superuser=True)
        admin.set_password('admin@123')
        admin.save()
        
        u1 = User.objects.create(username='Thanvith', role='candidate', display_name='Thanvith')
        u1.set_password('TCS@1234')
        u1.save()

        u2 = User.objects.create(username='Tejaswini', role='candidate', display_name='Tejaswini')
        u2.set_password('TCS@1234')
        u2.save()

        self.stdout.write('Database 100% wiped! Only admin1, Thanvith, and Tejaswini accounts remain.')
