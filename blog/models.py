# Think about the things you want save to database

from django.db import models
from django.utils import timezone # Import current time
from django.contrib.auth.models import User # post, user will have relationship, users will auth posts, one to many relationship

# Models
# Each class will be its own table in database
class Post(models.Model): # inheritence from models
	title = models.CharField(max_length=100)
	content = models.TextField() # Text field is unrestricted text
	date_posted = models.DateTimeField(default=timezone.now) # pass in actual function as defualt value
	author = models.ForeignKey(User, on_delete=models.CASCADE) # If user deleted, then we will delete post as well.
