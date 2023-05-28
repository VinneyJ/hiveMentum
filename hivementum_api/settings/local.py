from .base import * #noqa
from .base import env
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="adXu-Vlv76ko2ecdbZcMvn8U-MvKT_1ko4tO8yXDxGYiFP-Yqbg",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]