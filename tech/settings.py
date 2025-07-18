"""
Django settings for tech project.

Generated by 'django-admin startproject' using Django 4.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

from tutorial.settings import INSTALLED_APPS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j%4mc)jaxd_byb7)(3(&q_$ly0h)m+cqj+vbd)89d8d%6=@lt9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

SHARED_APPS = [
    'django_tenants',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'corsheaders',
    'rest_framework',

    # Your shared apps
    'subs',
    'base',
    'custom',
    'shop',
    'community',
    'pay',
    'agent'
]

TENANT_APPS = [
    'dashboard',
    'inventory',
    'payment',
    'themes',
    'cart',
    'hom',
    'service',
    'rooms',
    'portfolio',
    'bms',
    'skillsync',
    'todo',
    'editing',
]

INSTALLED_APPS = SHARED_APPS + TENANT_APPS  # No need to filter duplicates


# settings.py
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'tech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',  "templates/errors"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tech.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASE_ROUTERS = ('django_tenants.routers.TenantSyncRouter',)
TENANT_MODEL = "subs.Tenant"
TENANT_DOMAIN_MODEL = "subs.Domain"
SHOW_PUBLIC_IF_NO_TENANT_FOUND = True
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'saas',
        'USER': 'postgres',
        'PASSWORD': 'covid@2019',
        'HOST': 'localhost',  # Change if using a remote DB
        'PORT': '5432',  # Default PostgreSQL port
  }
 }

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]
AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',  # First priority
    'django.contrib.auth.backends.ModelBackend',  # Second priority
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CORS_ALLOW_ALL_ORIGINS = True


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React dev server
    "https://your-react-app.com",  # Optional production React app
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://your-react-app.com",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#MULTITENANT_RELATIVE_MEDIA_ROOT = "tenants/%s"

STORAGES = {
    "default": {
        "BACKEND": "django_tenants.files.storage.TenantFileSystemStorage", #"base.storage.CustomSchemaStorage",

    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SOCIALACCOUNT_AUTO_SIGNUP = False
SOCIALACCOUNT_PROVIDERS = {
     'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    },
    'github': {
        'APP': {
            'client_id': 'Ov23li5UIYdHimIcSs0W',
            'secret': '7355816b2c5dcad56bcb91967788b312c3e4b4d1',
            'key': ''
        }
    }
}
AUTH_USER_MODEL = 'custom.User'

AUTH_USER_MODEL = 'custom.CustomUser'

SITE_ID = 1


TENANT_MODEL = 'subs.Tenant'  # Replace 'your_app_name' with the actual app name

SOCIALACCOUNT_ADAPTER = 'custom.adapters.CustomSocialAdapter'

ACCOUNT_ADAPTER = 'custom.adapters.CustomAccountAdapter'
ACCOUNT_FORMS = {'signup': 'custom.forms.CustomUserSignupForm'}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'custom:redirect_after_login'  # Route to this view after login
LOGOUT_REDIRECT_URL = 'base:index'
ACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_QUERY_EMAIL = True

ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

  # Use SMTP to send emails
EMAIL_HOST = 'smtp.gmail.com'  # Gmail's SMTP server
EMAIL_PORT = 587  # SMTP port for Gmail
EMAIL_USE_TLS = True  # Use TLS for security
EMAIL_HOST_USER = 'wrldron@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'iuid ylaq qluc hdbf'  # App password if using 2FA
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Email address used as the sender