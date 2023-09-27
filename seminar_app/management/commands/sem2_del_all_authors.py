from django.core.management.base import BaseCommand
from seminar_app.models import Authors


class Command(BaseCommand):
    help = 'Delete all authors'

    def handle(self, *args, **kwargs):
        authors = Authors.objects.all()
        if authors is not None:
            authors.delete()
        self.stdout.write(f'{authors}')
