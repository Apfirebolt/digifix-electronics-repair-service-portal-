from django.core.management.base import BaseCommand, CommandError
from complaints.models import ReportIssue


class Command(BaseCommand):
    help = 'Deletes all created issues'

    def handle(self, *args, **options):
        try:
            issues = ReportIssue.objects.all()
            for issue in issues:
                issue.delete()
        except Exception as err:
            raise CommandError('Problem in deleting issue')