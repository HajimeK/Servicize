# Create your views here.
#from django import http
#
#def home(request):
#  return http.HttpResponse('Welcome to Chat')
from django.shortcuts import render_to_response
import datetime

def home(request):
  return render_to_response('chat/index.html', { 'clock': datetime.datetime.now()},)
