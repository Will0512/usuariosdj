# SECURITY WARNING: don't run with debug turned on in production!
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_seccret('DB_NAME'),
        'HOST': 'localhost',
        'USER': get_seccret('DB_USER'),
        'PASSWORD': get_seccret('DB_PASSWORD'),
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')