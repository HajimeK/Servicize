from django.db import models
from google.appengine.ext import ndb
import datetime

import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'lib'))
from wtforms.form import Form

class Chat(ndb.Model):
	subject = ndb.StringProperty()
	speaker = ndb.StringProperty()
	date = ndb.DateProperty()

obj = Chat(subject='please repair the machine', speaker='ABC')
#obj.date = datetime.date(2015,11,24)
form = Form()
form.populate_object(obj)
obj.put()

class ChatReview(ndb.Model):
	chat = ndb.KeyProperty(kind='Chat')
	reviewer = ndb.UserProperty()
	review_text = ndb.TextProperty()
	rating = ndb.StringProperty(choices=['Poor', 'OK', 'Good', 'Very Good', 'Great'], default = 'Great')
	create_data = ndb.DateTimeProperty(auto_now_add=True)
