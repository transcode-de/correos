from rest_framework import serializers

from .models import Domain, Email, Recipient


class DomainSerializer(serializers.HyperlinkedModelSerializer):
    users_count = serializers.IntegerField(
        # read_only, source are core arguments of IntegerFields
        # users is a foreignKey field of the model relation Domain-Recipient
        source='users.count',
        read_only=True
    )

    class Meta:
        model = Domain
        # uuid, name are attributes of model Domain
        # field, url are default fields of HlMSerializer instead of primary key
        fields = ('url', 'uuid', 'name', 'users_count')


class RecipientSerializer(serializers.HyperlinkedModelSerializer):
    emails_count = serializers.IntegerField(
        # emails is a foreignKey of the model relation Email-Recipient
        source='emails.count',
        read_only=True
    )

    class Meta:
        model = Recipient
        fields = ('url', 'uuid', 'email', 'realname', 'domain', 'emails_count')
        # Add depth of realtionships to be shown in nested representations
        depth = 1


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = ('url', 'uuid', 'message_id', 'sender', 'recipient',
                  'subject', 'date', 'is_multipart', 'header', 'body')
        depth = 2


'''
HyperlinkedModelSerializer is similar to ModelSerializer, but uses hyperlinks
to represent relationships rather than primary keys
ModelSerializer works like regular Serializer except that it will
automatically generate fields based on model, validators for serializer and
include default implementions of .create() and .update()
'''
