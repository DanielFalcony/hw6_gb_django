from django.core.management.base import BaseCommand
from seminar_app.models import Authors


class Command(BaseCommand):
    help = 'Get all authors'

    def handle(self, *args, **kwargs):
        authors = Authors.objects.all()
        self.stdout.write(f'{authors}')
