from random import randint

from django.core.management.base import BaseCommand
from seminar_app.models import GameModel


class Command(BaseCommand):
    help = 'Play game Head and Tails'

    def handle(self, *args, **kwargs):
        result = ('TAILS', 'HEAD')[randint(0, 1)]

        game = GameModel(result=result)
        game.save()

        self.stdout.write(f'{game}')
