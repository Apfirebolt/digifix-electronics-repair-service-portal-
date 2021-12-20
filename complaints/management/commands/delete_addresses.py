from django.core.management.base import BaseCommand, CommandError
from complaints.models import UserAddress


class Command(BaseCommand):
    help = 'Deletes all user addresses'

    def handle(self, *args, **options):
        try:
            addresses = UserAddress.objects.all()
            for address in addresses:
                address.delete()
        except Exception as err:
            raise CommandError('Problem in deleting address')