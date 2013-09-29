from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Email
from .serializers import EmailSerializer


class InboxView(TemplateView):
    template_name = 'correos/inbox.html'


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    filter_fields = ('sender', 'recipient', 'domain')
