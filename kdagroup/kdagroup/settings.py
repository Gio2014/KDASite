"""
Django settings for kdagroup project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9avwtj9tn*anthpm4yu7y(omwibuw3uzoyspa8w0)95-q0le2g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	#For Django 1.7+, use SimpleAdminConfig because we'll call autodiscover...
    'django.contrib.admin', #Because we're using Mandrill. Remove apps.SimpleAdminConfig when using something else.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kdagroup',
    'website',
    'sendgrid',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kdagroup.urls'

WSGI_APPLICATION = 'kdagroup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "/Users/giogomez2010/Documents/kdagroup.sqlite",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'



# Port for sending e-mail.

# Optional SMTP authentication information for EMAIL_HOST.
#EMAIL_BACKEND = 'sgbackend.SendGridBackend'
#EMAIL_HOST_USER = 'GioGomez2011'
#EMAIL_HOST_PASSWORD = 'FireFox09!!!'
#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'GioGomez2010'
EMAIL_HOST_PASSWORD = 'FireFox09!!!'
DEFAULT_FROM_EMAIL = ''
SERVER_EMAIL = 'root@localhost'

ADMINS = (
    ('Giovanni', 'giogomez2010@me.com'),
)