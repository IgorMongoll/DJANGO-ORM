from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from datetime import datetime
from social_app.models import User

class Command(BaseCommand):
    help = 'this is new custom command'
    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)
    def handle(self, *args: Any, **options: Any) :
        self.stdout.write('this is our command')
        print(datetime.now())
        users = User.objects.all()
        print(f'{len(users)} users subscribed in our website ')
        # for user in users:
        #     self.stdout.write(f'Username: {user.username}, Email: {user.email}, Bio: {user.bio}')