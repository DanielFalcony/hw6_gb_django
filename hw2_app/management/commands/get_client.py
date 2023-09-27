from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = 'Get Client by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.get(pk=pk)
        self.stdout.write(f'{client}')
