from optparse import make_option
import random

from django.conf import settings
from django.core.mail import get_connection, send_mail
from django.core.management.base import BaseCommand, CommandError

from ...utils import get_smtp_host

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

integer_elementum = """Integer elementum massa at nulla placerat varius. Suspendisse in libero risus, in interdum massa. Vestibulum ac leo vitae metus faucibus gravida ac in neque. Nullam est eros, suscipit sed dictum quis, accumsan a ligula.

In sit amet justo lectus. Etiam feugiat dolor ac elit suscipit in elementum orci fringilla. Aliquam in felis eros. Praesent hendrerit lectus sit amet turpis tempus hendrerit. Donec laoreet volutpat molestie. Praesent tempus dictum nibh ac ullamcorper. Sed eu consequat nisi.

Quisque ligula metus, tristique eget euismod at, ullamcorper et nibh. Duis ultricies quam egestas nibh mollis in ultrices turpis pharetra. Vivamus et volutpat mi. Donec nec est eget dolor laoreet iaculis a sit amet diam.
"""

proin_suscipit = """Proin suscipit luctus orci placerat fringilla. Donec hendrerit laoreet risus eget adipiscing. Suspendisse in urna ligula, a volutpat mauris. Sed enim mi, bibendum eu pulvinar vel, sodales vitae dui. Pellentesque sed sapien lorem, at lacinia urna.

In hac habitasse platea dictumst. Vivamus vel justo in leo laoreet ullamcorper non vitae lorem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin bibendum ullamcorper rutrum.
"""

messages = (
    ('Lorem ipsum', lorem_ipsum),
    ('Integer elementum massa at nulla', integer_elementum),
    ('Proin suscipit', proin_suscipit)
)

recipients_list = ('bob@example.com', 'cindy@example.com', 'dave@example.net',
    'eris@example.org', 'felix@example.org', 'hannah@example.net')

connection = get_connection(host=get_smtp_host(), port=settings.CORREOS_PORT)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--count', '-c', default=1, dest='count',
            help='Number of emails to send (default: "1").'),
    )
    help = ('Sends test email(s) to Correos\n\nEvery test email will be sent '
        'to a random number of recipients.')

    def handle(self, *args, **options):
        try:
            count = int(options['count'])
        except ValueError:
            raise CommandError('Only integers are allowed as --count option')
        while count > 0:
            recipients = random.sample(recipients_list,
                random.randint(1, len(recipients_list)))
            subject, message = random.sample(messages, 1)[0]
            send_mail(subject, message, 'alice@example.com', recipients,
                fail_silently=False, connection=connection)
            count -= 1
