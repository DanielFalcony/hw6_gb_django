import datetime
import random

from django.core.management.base import BaseCommand
from seminar_app.models import Authors, Post, Category


class Command(BaseCommand):
    help = 'Generate fake posts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for c in Category.objects.all():
            for a in Authors.objects.all():
                for i in range(1, count + 1):
                    post = Post(title=random.randint(1, 10),
                                post_text=random.randint(1, 10),
                                post_date='2000-01-01',
                                author=a,
                                category=c,
                                views=random.randint(1, 10),
                                publish=random.randint(0, 1))
                    post.save()
                    self.stdout.write(f'{post}')
