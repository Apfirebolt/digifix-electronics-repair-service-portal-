from django.core.management.base import BaseCommand, CommandError
from complaints.models import Comments


class Command(BaseCommand):
    help = 'Deletes all user comments'

    def handle(self, *args, **options):
        try:
            comments = Comments.objects.all()
            for comment in comments:
                comment.delete()
        except Exception as err:
            raise CommandError('Problem in deleting comment')