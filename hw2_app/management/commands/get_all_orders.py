from django.core.management.base import BaseCommand
from hw2_app.models import Order


class Command(BaseCommand):
    help = 'Get all Orders'

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for i in orders:
            self.stdout.write(f'{i}')
