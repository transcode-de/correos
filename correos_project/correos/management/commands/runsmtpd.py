import asyncore
from smtpd import SMTPServer
import sys

from django.core.management.base import BaseCommand
from django.conf import settings

from ...models import Email
from ...utils import get_smtp_host

localhost = get_smtp_host()


class CorreosSMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        if settings.CORREOS_SMTP_LOCAL and peer[0] not in (localhost,) + settings.INTERNAL_IPS:
            sys.stderr.write('Ignored email from host %s\n' % peer[0])
        else:
            emails = Email.objects.create_from_message(mailfrom, rcpttos, data)
            msg = 'Accepted email %s to %s from host %s\n'
            for email in emails:
                sys.stdout.write(msg % (email, email.recipient, peer[0]))


class Command(BaseCommand):
    help = 'Starts the Correos SMTP server'

    def handle(self, *args, **options):
        self.stdout.write('Starting SMTP server at %s:%s' % (localhost, settings.CORREOS_PORT))
        CorreosSMTPServer((localhost, settings.CORREOS_PORT), None)
        asyncore.loop()
