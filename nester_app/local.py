import os

from nester_app.settings import BASE_DIR

ALLOWED_HOSTS = ['localhost']

# DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = '73fuj9n8m+s*_76236aq&a03xw+10pfj08&&ifv&0-447y!ik$'