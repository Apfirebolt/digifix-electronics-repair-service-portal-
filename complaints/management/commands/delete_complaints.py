from django.core.management.base import BaseCommand, CommandError
from complaints.models import Complaint


class Command(BaseCommand):
    help = 'Deletes all complaints'

    def handle(self, *args, **options):
        try:
            complaints = Complaint.objects.all()
            for complaint in complaints:
                complaint.delete()
        except Exception as err:
            raise CommandError('Problem in deleting complaint')