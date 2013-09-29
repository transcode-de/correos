from django.db import models
from django.utils.timezone import now
from uuidfield import UUIDField

from .managers import EmailManager


class Domain(models.Model):
    uuid = UUIDField(auto=True, primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name


class Recipient(models.Model):
    uuid = UUIDField(auto=True, primary_key=True)
    email = models.EmailField(max_length=1000, unique=True)
    domain = models.ForeignKey(Domain, related_name='users')

    class Meta:
        ordering = ['domain', 'email']

    def __unicode__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.uuid:
            domain = '.'.join(self.email.split('@')[1].split('.')[-2:])
            self.domain, created = Domain.objects.get_or_create(name=domain)
        super(Recipient, self).save(*args, **kwargs)


class Email(models.Model):
    uuid = UUIDField(auto=True, primary_key=True)
    message_id = models.CharField(max_length=1000)
    sender = models.EmailField(max_length=1000)
    recipient = models.ForeignKey(Recipient, related_name='emails')
    subject = models.CharField(max_length=1000)
    date = models.DateTimeField()
    header = models.TextField()
    body = models.TextField()

    objects = EmailManager()

    class Meta:
        ordering = ['-date']
        unique_together = ('message_id', 'recipient')

    def __unicode__(self):
        return self.message_id

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = now()
        super(Email, self).save(*args, **kwargs)
