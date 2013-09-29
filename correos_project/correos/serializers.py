from rest_framework import serializers

from .models import Domain, Email, Recipient


class DomainSerializer(serializers.HyperlinkedModelSerializer):
    users_count = serializers.IntegerField(source='users.count', read_only=True)

    class Meta:
        model = Domain
        fields = ('url', 'uuid', 'name', 'users_count')


class RecipientSerializer(serializers.HyperlinkedModelSerializer):
    emails_count = serializers.IntegerField(source='emails.count', read_only=True)

    class Meta:
        model = Recipient
        fields = ('url', 'uuid', 'email', 'domain', 'emails_count')
        depth = 1


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = ('url', 'uuid', 'message_id', 'sender', 'recipient',
            'subject', 'date', 'header', 'body')
        depth = 2
