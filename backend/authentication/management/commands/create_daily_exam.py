"""
Management command: create_daily_exam

Creates today's exam with all 4 sections if it doesn't already exist.
Safe to run repeatedly — skips creation if today's exam already exists.

Usage:
    python manage.py create_daily_exam
    python manage.py create_daily_exam --date 2026-07-20
    python manage.py create_daily_exam --title "Day 42 — Practice"
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date


class Command(BaseCommand):
    help = 'Creates today\'s exam with 4 sections (arithmetic, verbal, reasoning, coding)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--date',
            type=str,
            help='Date for the exam (YYYY-MM-DD). Defaults to today.',
        )
        parser.add_argument(
            '--title',
            type=str,
            help='Custom exam title. Defaults to "Daily Practice — {date}".',
        )

    def handle(self, *args, **options):
        from exams.models import Exam, ExamSection
        from authentication.models import User

        target_date = date.today()
        if options['date']:
            try:
                from datetime import datetime
                target_date = datetime.strptime(options['date'], '%Y-%m-%d').date()
            except ValueError:
                self.stderr.write(self.style.ERROR('Invalid date format. Use YYYY-MM-DD.'))
                return

        # Check if exam already exists for this date
        existing = Exam.objects.filter(date=target_date).first()
        if existing:
            self.stdout.write(
                self.style.WARNING(
                    f'Exam already exists for {target_date}: "{existing.title}" (ID: {existing.id}, status: {existing.status})'
                )
            )
            return

        # Get admin user as creator
        admin_user = User.objects.filter(role='admin').first()

        # Build title
        title = options['title'] or f'Daily Practice — {target_date.strftime("%d %b %Y")}'

        # Create exam
        exam = Exam.objects.create(
            title=title,
            date=target_date,
            status='active',
            created_by=admin_user,
            description=f'Placement practice exam for {target_date.strftime("%d %B %Y")}. '
                        f'4 sections: Arithmetic, Verbal, Reasoning, and Coding.'
        )

        # Create 4 sections with standard placement exam configuration
        SECTIONS = [
            {
                'section_type': 'arithmetic',
                'order': 1,
                'duration_minutes': 20,
                'max_score': 100,
                'question_count': 25,
            },
            {
                'section_type': 'verbal',
                'order': 2,
                'duration_minutes': 20,
                'max_score': 80,
                'question_count': 20,
            },
            {
                'section_type': 'reasoning',
                'order': 3,
                'duration_minutes': 20,
                'max_score': 100,
                'question_count': 25,
            },
            {
                'section_type': 'coding',
                'order': 4,
                'duration_minutes': 60,
                'max_score': 200,
                'question_count': 2,
            },
        ]

        for section_data in SECTIONS:
            ExamSection.objects.create(exam=exam, **section_data)
            self.stdout.write(f'  Created section: {section_data["section_type"]}')

        self.stdout.write(self.style.SUCCESS(
            f'\nExam created successfully!'
            f'\n  Title   : {exam.title}'
            f'\n  Date    : {exam.date}'
            f'\n  Status  : {exam.status}'
            f'\n  Exam ID : {exam.id}'
            f'\n  URL     : http://127.0.0.1:8000/admin/exams/exam/{exam.id}/change/'
        ))
