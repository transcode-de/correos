from django.db import models
from django.utils.timezone import now
from uuidfield import UUIDField

from .managers import EmailManager


class Email(models.Model):
    uuid = UUIDField(auto=True, primary_key=True)
    message_id = models.CharField(max_length=1000)
    sender = models.CharField(max_length=1000)
    recipient = models.CharField(max_length=1000)
    domain = models.CharField(max_length=200)
    subject = models.CharField(max_length=1000)
    date = models.DateTimeField()
    header = models.TextField()
    body = models.TextField()

    objects = EmailManager()

    def __unicode__(self):
        return self.message_id

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.domain = '.'.join(self.recipient.split('@')[1].split('.')[-2:])
        if self.date is None:
            self.date = now()
        return super(Email, self).save(*args, **kwargs)
