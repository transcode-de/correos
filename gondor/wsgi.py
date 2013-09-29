"""Gondor WSGI config for correos project.
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'correos_project'))
sys.path.insert(0, BASE_DIR)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
