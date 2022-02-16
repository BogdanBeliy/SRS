import django

django.setup()
from django.core.management.base import BaseCommand
from core.utils.data_utils import AddFakeData


class Command(BaseCommand):
    hepl = 'Create or remove data'

    def handle(self, *args, **options):
        fake = AddFakeData()
        # if options['delete']:
        #     fake.remove_all()
        if options['create']:
            fake.run()
        elif options['delete']:
            fake.remove_all()
        else:
            print('No argements')

    def add_arguments(self, parser):
        parser.add_argument(
            '-d',
            '--delete',
            action='store_true',
            default=False,
            help='Удалить все категории и обьявления'
        )
        parser.add_argument(
            '-c',
            '--create',
            action='store_true',
            default=False,
            help='Создать фейковые категории и обьявления'
        )


if __name__ == '__main__':
    Command().handle()
