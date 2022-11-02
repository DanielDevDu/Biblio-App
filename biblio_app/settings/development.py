from .base import *

# Email settings
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_PORT = env("EMAIL_PORT")
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "danieldevdu@gmail.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "BiBlioApp"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": env("POSTGRES_ENGINE"),
#         "NAME": env("POSTGRES_DB"),
#         "USER": env("POSTGRES_USER"),
#         "PASSWORD": env("POSTGRES_PASSWORD"),
#         "HOST": env("PG_HOST"),
#         "PORT": env("PG_PORT"),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# GRAPH_MODELS = {
#     "all_applications": True,
#     "group_models": True,
# }

# Login settings
# LOGIN_REDIRECT_URL = '/admin'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_PORT = env("EMAIL_PORT")
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_USE_TLS = env("EMAIL_USE_TLS")

EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER="danieldevdu@gmail.com"
EMAIL_HOST_PASSWORD="ecpkbygtnxnvqjih"
EMAIL_PORT=587
EMAIL_USE_TLS=True

# Celery settings
# CELERY_BROKER_URL = env("CELERY_BROKER")
# CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
# CELERY_TIMEZONE = "America/Bogota"