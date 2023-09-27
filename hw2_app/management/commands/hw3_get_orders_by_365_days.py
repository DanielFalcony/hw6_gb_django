from datetime import timedelta, datetime
from django.core.management.base import BaseCommand
from hw2_app.models import Order, Goods


class Command(BaseCommand):
    help = 'Get products from a specific customer\'s orders for the last 30 days.'

    def add_arguments(self, parser):
        parser.add_argument('client', type=str, help='client ID')

    def handle(self, *args, **kwargs):
        client = kwargs['client']
        year_ago = datetime.now() - timedelta(days=365)
        orders = Order.objects.filter(client=client, order_date__gte=year_ago).order_by('-order_date')

        if orders.exists():
            products = Goods.objects.filter(order__in=orders).distinct()
            result = '\n'.join(f'{i + 1}. {product}' for i, product in enumerate(products))
            self.stdout.write(result)
        else:
            self.stdout.write(f'Customer ID {client} has not placed any orders in the last 7 days.')
