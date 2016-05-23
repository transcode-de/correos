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
        # peer = remotes hosts adress(IP, incoming port),
        # mailfrom = envelope, from-information given to server by client
        # rcpttos = recipients, data = string containing content acc. RFC5321
        # Ignores emails send by hosts other than local
        # Creates entities of Email from received messages
        # Returns a list of Email objects
        if (settings.CORREOS_SMTP_LOCAL and
                peer[0] not in (localhost,) + settings.INTERNAL_IPS):
                    sys.stderr.write('Ignored email from host %s\n' % peer[0])
        else:
            emails = Email.objects.create_from_message(mailfrom, rcpttos, data)
            msg = 'Accepted email %s to %s from host %s\n'
            for email in emails:
                sys.stdout.write(msg % (email, email.recipient, peer[0]))


# Command must be implemented to enable the command "runsmtpd"
class Command(BaseCommand):
    help = 'Starts the Correos SMTP server'

    # Keeps the actual logic of the command "runsmtpd"
    def handle(self, *args, **options):
        self.stdout.write(
            'Starting SMTP server at %s:%s' % (
                localhost, settings.CORREOS_PORT
            )
        )
        # Instantiates the SMTPserver with local address (localhost) and
        # port (by default 1025)
        CorreosSMTPServer((localhost, settings.CORREOS_PORT), None)
        # Enters a polling loop in the network channel
        asyncore.loop()


''' SMTPServer
* inherits from asyncore.dispatcher
* asyncore.dispatcher is a wrapper around low-level socket object, has few
    methods for event-handling called from asynchronous loop, otherwise
    non-blocking socket object
* loop() enters a polling loop in a network channel stored in global map
    created by asyncore.dispatcher and asynchat.async_chat,
    terminates only after count (optional argument) passes or all open channels
    have been closed
'''
