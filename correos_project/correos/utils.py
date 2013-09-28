import socket

from django.conf import settings


def get_smtp_host():
    """Returns the hostname to use fpr SMTP."""
    if settings.CORREOS_USE_PUBLIC_IP:
        host = socket.gethostbyname(socket.gethostname())
    else:
        host = '127.0.0.1'
    return host
