import django

django.setup()
from django.core.management.base import BaseCommand
from core.utils.data_create_utils import pr


class Command(BaseCommand):
    hepl = 'x'
    def handle(self, *args, **options):
        pr()

if __name__ == '__main__':
    Command().handle()
