from django.core.management.base import BaseCommand
from hw2_app.management.commands.fake_date import generate_random_date
import random

from hw2_app.models import Goods


class Command(BaseCommand):
    help = 'Generate fake goods'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        goods_list = ['Table', 'Lamp', 'Flashlight', 'Backpack', 'Toilet', 'Razor']
        for i in range(1, count + 1):
            good = Goods(product_name=f'{random.choice(goods_list)}',
                         product_description=f'Some description{i} bla bla bla',
                         product_price=f'{random.uniform(1, 500):.2f}',
                         product_quantity=f'{random.randint(1, 100)}',
                         date_item_add=generate_random_date(2022, 2023), )
            good.save()
            self.stdout.write(f'{good}')
