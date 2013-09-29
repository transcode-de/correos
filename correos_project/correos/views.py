from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Domain, Email
from . import serializers


class InboxView(TemplateView):
    template_name = 'correos/inbox.html'


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = serializers.DomainSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = serializers.EmailSerializer
    filter_fields = ('sender', 'recipient', 'domain')
