from django.core.management.base import BaseCommand
from seminar_app.models import Post


class Command(BaseCommand):
    help = 'Get all Posts'

    def handle(self, *args, **kwargs):
        res = Post.objects.all()
        posts = [str(post) for post in res][:5]
        for i in posts:
            self.stdout.write(f'{i}', ending='\n')
