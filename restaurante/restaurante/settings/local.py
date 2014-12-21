from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'restaurante',
        'USER': 'rest',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


STATIC_URL = '/static/'

MEDIA_URL = 'media'

MEDIA_ROOT = BASE_DIR.child('media')