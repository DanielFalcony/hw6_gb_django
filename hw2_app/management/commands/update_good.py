from django.core.management.base import BaseCommand
from hw2_app.models import Goods


class Command(BaseCommand):
    help = 'Update Good by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Good ID')
        parser.add_argument('product_name', type=str, help='Good Name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product_name = kwargs.get('product_name')
        good = Goods.objects.filter(pk=pk).first()
        if good is not None:
            good.product_name = product_name
            good.save()
            self.stdout.write(f'Client:"{good}" update successful!')
        else:
            self.stdout.write(f'No client with this ID')
