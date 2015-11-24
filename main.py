import os
#from os.path import abspath, dirname
import django.core.handlers.wsgi
import sys

os.environ["DJANGO_SETTINGS_MODULE"] = "Servicize2.settings"
sys.path.append('lib')
# Following did not solve the problem, even lib specifies the correct abs path. Mayby issue of python
#sys.path.append(os.path.join(abspath(os.path.join(dirname(__file__),".")),'lib'))
#sys.path.append(os.path.join(os.getcwd(), 'lib'))

application = django.core.handlers.wsgi.WSGIHandler()