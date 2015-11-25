from django.db import models
from google.appengine.ext import ndb

class Chat(ndb.Model):
	subject = ndb.StringProperty()
	speaker = ndb.StringProperty()
	date = ndb.DateProperty()

class ChatReview(ndb.Model):
	chat = ndb.KeyProperty(kind='Chat')
	reviewer = ndb.UserProperty()
	review_text = ndb.TextProperty()
	rating = ndb.StringProperty(choices=['Poor', 'OK', 'Good', 'Very Good', 'Great'], default = 'Great')
	create_data = ndb.DateTimeProperty(auto_now_add=True)
