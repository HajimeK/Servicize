from django.db import models

# Create your models here.
from google.appengine.ext
import ndb

class Chat(ndb.Model):
	Subject = ndb.StringProperty()
	Speaker = ndb.StringProperty()
	date = ndb.DateProperty()

class ChatReview(ndb.Model):
	chat = ndb.KeyPropery(kind='Chat')
    reviewer = ndb.UserProperty()
	review_text = ndb.TextProperty()
	rating = ndb.StringProperty(Choices=['Poor', 'OK', 'Good', 'Very Good', 'Great'], default = 'Great')
	create_data = ndb.DateTimePropery(auto_now_add=True)