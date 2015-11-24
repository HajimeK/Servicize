# Create your views here.
#from django import http
#
#def home(request):
#  return http.HttpResponse('Welcome to Chat')
from django import template
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from google.appengine.ext import ndb

import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'lib'))

from wtforms_appengine.ndb import model_form

from chat import models
import datetime

def home(request):
  return render_to_response('chat/index.html', {'clock': datetime.datetime.now()},)
  return render_to_response('chat/index.html', {'clock': q},)

ChatForm = model_form(models.Chat)

def form(request, chat_id=None):
  q = models.Chat.query().order('subject')
  if request.method =='POST':
      if chat_id:
         chat = models.Chat.get_by_id(int(chat_id))
         form = ChatForm(request.POST, obj=chat)
      else:
         chat = models.Chat()
         form = ChatForm(request.POST)
         
      if form.Validate():
        form.populate_obj(chat)
        chat.put()
        return HttpResponseRedirect('/chat/')

  else:
     if chat_id:
       chat = models.Chat.get_by_id(int(chat_id))
       form = ChatForm(obj=chat)
     else:
       form = ChatForm()
       
  return render_to_response('chat/chatform.html', {
            'chat_id': chat_id,
            'form': form,
  }, template.RequestContext(request))