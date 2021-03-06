from django.db import models
from django.utils.timezone import now
from uuidfield import UUIDField

from .managers import EmailManager


class Domain(models.Model):
    uuid = UUIDField(auto=True, primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name


class Recipient(models.Model):
    uuid = UUIDField(auto=True, primary_key=True)
    email = models.EmailField(unique=True)
    realname = models.CharField(max_length=255)
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
    sender = models.EmailField()
    recipient = models.ForeignKey(Recipient, related_name='emails')
    subject = models.CharField(max_length=1000)
    date = models.DateTimeField()
    is_multipart = models.BooleanField()
    header = models.TextField()
    body = models.TextField()
    is_read = models.BooleanField(default=False)

    objects = EmailManager()

    class Meta:
        ordering = ['-date']
        unique_together = ('message_id', 'recipient')

    def __unicode__(self):
        return '%s for %s' % (self.message_id, self.recipient)

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = now()
        super(Email, self).save(*args, **kwargs)
