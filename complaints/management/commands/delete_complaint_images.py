from django.core.management.base import BaseCommand, CommandError
from complaints.models import ComplaintImages


class Command(BaseCommand):
    help = 'Deletes all complaint images'

    def handle(self, *args, **options):
        try:
            complaint_images = ComplaintImages.objects.all()
            for complaint_image in complaint_images:
                complaint_image.delete()
        except Exception as err:
            raise CommandError('Problem in deleting complaint image')