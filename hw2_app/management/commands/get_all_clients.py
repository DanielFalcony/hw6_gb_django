from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = 'Get all Clients'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for i in clients:
            self.stdout.write(f'{i}')
