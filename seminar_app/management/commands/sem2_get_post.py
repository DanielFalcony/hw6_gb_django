from django.core.management.base import BaseCommand
from seminar_app.models import Post


class Command(BaseCommand):
    help = 'Get all Posts'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        self.stdout.write(f'{post}')
