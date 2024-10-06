import os
import sys

path = '/home/yourusername/assign-2-local-library-part-2-dcook486'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'locallibrary.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
