import datetime
import random

from django.core.management.base import BaseCommand
from seminar_app.models import Authors


class Command(BaseCommand):
    help = 'Generate fake authors and posts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Authors(name=f'Name{i}', last_name=f'last_name{i + 1}', email=f'{i + i + 1}@mail.ru',
                             biography=f'biography of {i} is bla-bla-bla...',
                             birthday='2000-01-12')
            author.save()
