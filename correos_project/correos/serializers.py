from rest_framework import serializers

from .models import Domain, Email


class DomainSerializer(serializers.ModelSerializer):
    emails_count = serializers.IntegerField(source='emails.count', read_only=True)

    class Meta:
        model = Domain


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        exclude = ('domain',)
