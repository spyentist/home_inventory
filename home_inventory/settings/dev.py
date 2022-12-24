from .main_settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inventory',
        'USER': 'root',
        'PASSWORD': 'Password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}