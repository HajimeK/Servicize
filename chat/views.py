# Create your views here.
#from django import http
#
#def home(request):
#  return http.HttpResponse('Welcome to Chat')
from django.shortcuts import render_to_response
import datetime

def home(request):
  q = models.Chat.order('Subject')
  return render_to_response('chat/index.html', {'clock': datetime.datetime.now()},)

ChatForm = model_form(models.Chat)

def form(request):