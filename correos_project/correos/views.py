from dateutil.parser import parse
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
    model = Email
    serializer_class = serializers.EmailSerializer
    filter_fields = ('sender', 'recipient__email')
    paginate_by = 20
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    def get_queryset(self):
        """Optionally filters the emails using the `after` query parameter."""
        qs = Email.objects.all()
        after = self.request.QUERY_PARAMS.get('after', None)
        if after is not None:
            qs = qs.filter(date__gt=parse(after))
        return qs
