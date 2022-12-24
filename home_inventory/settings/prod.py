from .main_settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('mysql_NAME'),
        'USER': os.environ.get('mysql_USER'),
        'PASSWORD': os.environ.get('mysql_PASSWORD'),
        'HOST': 'mysql_db',
        'PORT': '3306',
    },


}

