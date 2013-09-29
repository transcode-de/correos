from django.conf.urls import patterns, include, url

from .views import InboxView

urlpatterns = patterns('',
    url(r'^$', InboxView.as_view(), name='correos_inbox'),
)
