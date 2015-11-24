import os
os.environ["DJANGO_SETTINGS_MODULE"] = "Servicize2.settings"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

import sys
sys.path.append('lib')