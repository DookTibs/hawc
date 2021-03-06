"""
Update settings for rapid-unit-testing:

python manage.py test --settings=hawc.settings.unittest

"""
from .local import *  # noqa

import logging


DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'hawc_test',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


logging.disable(logging.CRITICAL)


class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return 'notmigrations'


MIGRATION_MODULES = DisableMigrations()
