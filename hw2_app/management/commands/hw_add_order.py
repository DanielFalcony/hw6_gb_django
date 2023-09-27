from django.core.management.base import BaseCommand

from hw2_app.management.commands.fake_date import generate_random_date
from hw2_app.models import Goods, Client, Order
import random


class Command(BaseCommand):
    help = 'Generate fake orders'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count Orders')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            order = Order(client=random.choice(Client.objects.all()), total_price=0,
                          order_date=(generate_random_date(2022, 2023)), )
            order.save()
            select_goods = [random.choice(Goods.objects.all()) for i in range(5)]
            for good in select_goods:
                order.goods.add(good)
            order.total_price = sum(good.product_price for good in select_goods)
            order.save()
            self.stdout.write(f'Fake order: "{order}" add')
