from django.core.management.base import BaseCommand
from hw2_app.models import Goods


class Command(BaseCommand):
    help = 'Get all Goods'

    def handle(self, *args, **kwargs):
        goods = Goods.objects.all()
        for i in goods:
            self.stdout.write(f'{i}')
