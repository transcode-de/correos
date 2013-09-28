from email import message_from_string
import json

from django.db import models
from dateutil.parser import parse


class EmailManager(models.Manager):
    def create_from_message(self, mailfrom, rcpttos, data):
        message = message_from_string(data)
        emails = []
        for rcptto in rcpttos:
            email = self.model(sender=mailfrom, recipient=rcptto)
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
