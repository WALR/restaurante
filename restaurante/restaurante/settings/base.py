from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = '@n-0p-!5)ba1-zcr$d3us-7nw2c6z9b&d!e0tuoc#17jgb%hk='


DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    )

LOCAL_APPS = (

    )

THIRD_PARTY_APPS = (

    )

INSTALLED_APPS = DJANGO_APPS+LOCAL_APPS+THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'restaurante.urls'

WSGI_APPLICATION = 'restaurante.wsgi.application'

LANGUAGE_CODE = 'es-GT'
TIME_ZONE = 'America/Guatemala'
USE_I18N = True
USE_L10N = True
USE_TZ = True