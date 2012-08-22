# Copy this file to settings.py.
from settings_default import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


API_RENDER_HTML = True
INSTALLED_APPS = INSTALLED_APPS + ('djangorestframework', )

PERMISSION_CLASS = 'custom_permissions.CustomPermissions'
