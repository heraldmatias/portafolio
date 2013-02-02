
from project.settings import *
DEBUG=True
TEMPLATE_DEBUG=DEBUG

try:
    from _settings import *
except:
    pass

import sys

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
