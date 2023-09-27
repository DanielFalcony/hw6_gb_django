from django.core.management.base import BaseCommand
from hw2_app.models import Goods


class Command(BaseCommand):
    help = 'Delete good by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Good ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        good = Goods.objects.get(pk=pk)
        good.delete()

        self.stdout.write(f'Delete good:{good} successful!')
