from django.conf.urls import patterns, include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'domain', views.DomainViewSet)
router.register(r'user', views.RecipientViewSet)
router.register(r'email', views.EmailViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^$', views.InboxView.as_view(), name='correos_inbox'),
)
