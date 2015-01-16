"""
Django settings for blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from YamJam import yamjam
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    selected_configuration = 'development'
else:
    selected_configuration = 'deployment'
#Picks specific configuration
cfg = yamjam('/Users/varunmehta/.yamjam/config_blog.yaml')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = cfg[selected_configuration]['secret_key']

TEMPLATE_DEBUG = cfg[selected_configuration]['template_debug']

ALLOWED_HOSTS = cfg[selected_configuration]['allowed_hosts']


# Application definition
INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Apps Installed for System Optimization
    'django_jinja',
    'debug_toolbar',
    'blog_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# TEMPLATE_LOADERS = (
#     ('django.template.loaders.cached.Loader',
#         (
#             'django.template.loaders.filesystem.Loader',
#             'django.template.loaders.app_directories.Loader',
#         )
#     ),
# )

# Template loaders for django-jinja
TEMPLATE_LOADERS = (
    'django_jinja.loaders.FileSystemLoader',
    'django_jinja.loaders.AppLoader',
)

DEFAULT_JINJA2_TEMPLATE_INTERCEPT_RE = r"^(?!(admin|debug_toolbar|grappelli)/).*" #works for other than admin & debug_toolbar
# DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'

TEMPLATE_DIRS = ('blog_app/templates/blog_app',)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth'
)
ROOT_URLCONF = 'blog.urls'

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': cfg[selected_configuration]['database']['engine'],
        'NAME': cfg[selected_configuration]['database']['name'],
        'USER': cfg[selected_configuration]['database']['user'],
        'PASSWORD': cfg[selected_configuration]['database']['password'],
        'HOST': cfg[selected_configuration]['database']['host'],
        'PORT': cfg[selected_configuration]['database']['port'],
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

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'blog/static'),
)

GRAPPELLI_ADMIN_TITLE = 'Blog CMS'
GRAPPELLI_INDEX_DASHBOARD = 'blog.dashboard.CustomIndexDashboard'
