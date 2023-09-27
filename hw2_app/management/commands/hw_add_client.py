from django.core.management.base import BaseCommand

from hw2_app.management.commands.fake_date import generate_random_date
from hw2_app.models import Client


class Command(BaseCommand):
    help = 'Generate fake clients'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'John{i}',
                            email=f'a{i}b@mail.ru',
                            phone_number=f'{i * 3945512}',
                            address=f'some address house.{i}',
                            reg_date=generate_random_date(2022, 2023), )
            client.save()
            self.stdout.write(f'{client}')
