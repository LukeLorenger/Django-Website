from django.db import models
from django.contrib.auth.models import User # extending existing user model

# New Model, inherit from models.Model
class Profile(models.Model):
	#OnetoOne relationship with existing user model
	user = models.OneToOneField(User, on_delete=models.CASCADE) # personal user data to be deleted w/ user
	image = models.ImageField(default='default.jpg', upload_to='profile_pics') # Image field

	# dunder str method
	def __str__(self): # takes self as args, self is instance 
		return f'{self.user.username} Profile' # everytime profile is printed, it will print username
