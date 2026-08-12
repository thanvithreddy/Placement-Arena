from django.test import TestCase
from datetime import date
from authentication.models import User
from exams.models import Exam, ExamSection, ExamAttempt, SectionAttempt

from rest_framework.test import APITestCase, APIClient

class ExamResultViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.exam = Exam.objects.create(title='Test Exam', date=date.today(), status='active')
        self.section1 = ExamSection.objects.create(exam=self.exam, section_type='arithmetic', order=1, duration_minutes=20, max_score=40, question_count=20)
        self.section2 = ExamSection.objects.create(exam=self.exam, section_type='verbal', order=2, duration_minutes=20, max_score=40, question_count=20)
        self.attempt = ExamAttempt.objects.create(user=self.user, exam=self.exam, status='completed', total_score=50)
        self.sa1 = SectionAttempt.objects.create(exam_attempt=self.attempt, section=self.section1, score=25, status='completed')
        self.sa2 = SectionAttempt.objects.create(exam_attempt=self.attempt, section=self.section2, score=25, status='completed')
        self.client = APIClient()

    def test_exam_result_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/exams/{self.exam.id}/result/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['total_max_score'], 80)
        self.assertEqual(data['total_score'], 50)
