from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = 'Update Client by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client Name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.name = name
            client.save()
            self.stdout.write(f'Client:"{client}" update successful!')
        else:
            self.stdout.write(f'No client with this ID')
