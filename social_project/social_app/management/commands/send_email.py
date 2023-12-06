from django.core.mail import send_mail
from django.http import HttpResponse
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from datetime import datetime


def send_email_view(request):
    subject = 'Email Subject'
    message = 'Email Text.'
    from_email = 'davidundigor@gmail.com'
    
    recipient_list = ['igor.gurov@arcor.de']

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Email successfully sent!')

class Command(BaseCommand):
    help = 'this is new custom command'
    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)
    
    def handle(self, *args: Any, **options: Any) :
        subject = 'Email Subject'
        message = 'Email Text.'
        from_email = 'davidundigor@gmail.com'
        
        recipient_list = ['igor.gurov@arcor.de']

        send_mail(subject, message, from_email, recipient_list)
