from django.core.management.base import BaseCommand
from authentication.models import User

class Command(BaseCommand):
    help = 'Ensures admin1, Thanvith, and Tejaswini user accounts exist safely without modifying questions or exam data.'

    def handle(self, *args, **kwargs):
        # 1. Create Admin User if missing
        if not User.objects.filter(username='admin1').exists():
            admin = User.objects.create(username='admin1', role='admin', display_name='Admin User', is_staff=True, is_superuser=True)
            admin.set_password('admin@123')
            admin.save()
            self.stdout.write('Created default admin account: admin1')

        # 2. Create Candidate Thanvith if missing
        if not User.objects.filter(username='Thanvith').exists():
            u1 = User.objects.create(username='Thanvith', role='candidate', display_name='Thanvith')
            u1.set_password('TCS@1234')
            u1.save()
            self.stdout.write('Created default candidate account: Thanvith')

        # 3. Create Candidate Tejaswini if missing
        if not User.objects.filter(username='Tejaswini').exists():
            u2 = User.objects.create(username='Tejaswini', role='candidate', display_name='Tejaswini')
            u2.set_password('TCS@1234')
            u2.save()
            self.stdout.write('Created default candidate account: Tejaswini')

        self.stdout.write('Initial default user check complete! No existing data altered.')
