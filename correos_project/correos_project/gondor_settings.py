import os

import dj_database_url

from .settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['kg358.gondor.co', 'localhost']

# Make this unique, and don't share it with anybody.
# You can use this command to create a 50 char random key:
# python -c "import os; print(os.urandom(52).encode('base64')[:50])"
SECRET_KEY = os.environ['SECRET_KEY']

MEDIA_ROOT = os.path.join(os.environ['GONDOR_DATA_DIR'], 'site_media', 'media')
STATIC_ROOT = os.path.join(os.environ['GONDOR_DATA_DIR'], 'site_media', 'static')

# These two settings define what URLs your application knows about where
# servable files are located. Make sure the URLs used here are mapped in
# your gondor.yml under static_files.
MEDIA_URL = '/site_media/media/'
STATIC_URL = '/site_media/static/'

DATABASES = {
    'default': dj_database_url.config(env='GONDOR_DATABASE_URL'),
}

# Change if the server is in a different timezone.
TIME_ZONE = 'Europe/Berlin'

SITE_ID = 1

LOGGING.update({
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    }
})
