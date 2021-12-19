from django.core.management.base import BaseCommand, CommandError
from complaints.models import UserTestimonials


class Command(BaseCommand):
    help = 'Deletes all user testimonials'

    def handle(self, *args, **options):
        try:
            testimonials = UserTestimonials.objects.all()
            for testimonial in testimonials:
                testimonial.delete()
        except Exception as err:
            raise CommandError('Problem in deleting testimonial')