from django.views.generic import TemplateView
from rest_framework import viewsets

from . import serializers
from .models import Domain, Email, Recipient


class InboxView(TemplateView):
    template_name = 'correos/inbox.html'


class DashboardView(TemplateView):
    template_name = 'correos/dashboard.html'


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = serializers.DomainSerializer


class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = serializers.RecipientSerializer
    filter_fields = ('domain__name',)


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = serializers.EmailSerializer
    filter_fields = ('sender', 'recipient__email')
    paginate_by = 20
    paginate_by_param = 'page_size'
    max_paginate_by = 100
