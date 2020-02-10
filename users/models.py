from django.db import models
from django.contrib.auth.models import User # extending existing user model
from PIL import Image

# New Model, inherit from models.Model
class Profile(models.Model):
	#OnetoOne relationship with existing user model
	user = models.OneToOneField(User, on_delete=models.CASCADE) # personal user data to be deleted w/ user
	image = models.ImageField(default='default.jpg', upload_to='profile_pics') # Image field

	# dunder str method
	def __str__(self): # takes self as args, self is instance 
		return f'{self.user.username} Profile' # everytime profile is printed, it will print username

	def save(self):
		super().save() # running save method from parent class

		img = Image.open(self.image.path) # Will open image of current instance

		if img.height > 300 or img.width > 300: # If image is greater than 300x300 
			output_size = (300, 300) # saving prefered output size in output_size
			img.thumbnail(output_size) # passing in output_size to thumbnail to change size of img
			img.save # save img


