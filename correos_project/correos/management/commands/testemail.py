from django.conf import settings
from django.core.mail import get_connection, send_mail
from django.core.management.base import BaseCommand

from ...utils import get_smtp_host

message = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

connection = get_connection(host=get_smtp_host(), port=settings.CORREOS_PORT)


class Command(BaseCommand):
    help = 'Sends a test email to Correos'

    def handle(self, *args, **options):
        send_mail('Correos Test', message, 'alice@example.com',
            ['bob@example.com', 'cindy@example.com'], fail_silently=False,
            connection=connection)
