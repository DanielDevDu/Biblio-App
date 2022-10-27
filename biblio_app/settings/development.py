from .base import *

# Email settings
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "info@realestate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Real Estate"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Celery settings
# CELERY_BROKER_URL = env("CELERY_BROKER")
# CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
# CELERY_TIMEZONE = "America/Bogota"