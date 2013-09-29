from email import message_from_string, utils
import json

from django.db import models
from dateutil.parser import parse


class EmailManager(models.Manager):
    def create_from_message(self, mailfrom, rcpttos, data):
        from .models import Recipient
        message = message_from_string(data)
        realnames = {}
        for rcptto in message['To'].split(','):
            realname, email = utils.parseaddr(rcptto)
            realnames[email] = realname
        emails = []
        for rcptto in rcpttos:
            recipient, created = Recipient.objects.get_or_create(email=rcptto,
                defaults={'realname': realnames[rcptto]})
            email = self.model(sender=mailfrom, recipient=recipient)
            email.date = message.get('Date')
            if email.date is not None:
                email.date = parse(email.date)
            email.message_id = message['Message-ID']
            email.subject = message['Subject']
            email.header = json.dumps(dict(message.items()))
            email.body = message.get_payload()
            email.save()
            emails.append(email)
        return emails
