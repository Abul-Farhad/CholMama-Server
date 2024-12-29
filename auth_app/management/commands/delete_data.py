from django.core.management.base import BaseCommand
from auth_app.models import UserAccount, UserProfile

class Command(BaseCommand):
    help = 'Delete all data from UserAccount and UserProfile tables'

    def handle(self, *args, **kwargs):
        UserProfile.objects.all().delete()
        UserAccount.objects.all().delete()
        self.stdout.write("All data deleted successfully!")
