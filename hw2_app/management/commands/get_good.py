from django.core.management.base import BaseCommand
from hw2_app.models import Goods


class Command(BaseCommand):
    help = 'Get Good by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Good ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        good = Goods.objects.get(pk=pk)
        self.stdout.write(f'{good}')
