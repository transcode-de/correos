from email import message_from_string, utils
import json

from django.db import models
from dateutil.parser import parse


'''extra Manager for table-level functionality of model Email, returns a list
    of entities of Email'''


class EmailManager(models.Manager):
    def create_from_message(self, mailfrom, rcpttos, data):
        # Imported here to avoid circulate import callings
        from .models import Recipient
        # Returns a message object structure from a string
        message = message_from_string(data)
        # Declares a dict for realnames and corresponding emailaddresses
        realnames = {}
        # Iterates all recipients included in message
        for rcptto in message['To'].split(','):
            # Parts name from email, returns a 2-tuple
            realname, email = utils.parseaddr(rcptto)
            # If no realname, email address is used without @
            if len(realname) == 0:
                realname = email.split('@')[0]
            realnames[email] = realname

        # Declares a list for Email entities to be returned
        emails = []
        for rcptto in rcpttos:
            # Checks if this recipient already exists, if not, creates a new
            recipient, created = Recipient.objects.get_or_create(
                email=rcptto,
                defaults={'realname': realnames[rcptto]}
            )
            # Assigns attributes to entity of class Email
            email = self.model(sender=mailfrom, recipient=recipient)
            email.date = message.get('Date')
            if email.date is not None:
                email.date = parse(email.date)
            email.is_multipart = message.is_multipart()
            email.message_id = message['Message-ID']
            email.subject = message['Subject']
            email.header = json.dumps(dict(message.items()))
            email.body = message.get_payload()
            email.save()
            emails.append(email)
        return emails


'''
* email package
    = managing email messages incl. MIME and other RFC 2822 based message docs
    = NOT designed for sending Email to SMTP (RFC 2821),for that: modul smtplib
    = splits parsing and generating of email msg from the internal object model
      representation of email

* email.message_from_string()
    = returns a msg object structure from a string (same like
        Parser().parsestr(), wrapping text in StringIO and calling parse()),
        parse(fp, headersonly=False) reads data from the file-like object fp,
        parses the text and returns the root msg. object,
        fp must support readline() and read() methods on file-like objects,
        text in fp must be formatted as block of RFC 2822 style headers and
        header continuation lines, optionally envelope header

* utils.parseaddr()
    = parses address (To or CC) into realname and email address parts, returns
        2-tuple of ('', '')

* json.dumps(obj)
    = serialzies obj to a JSON formatted str using a conversation table (Python
        dict --> JSON object)
'''
