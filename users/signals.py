# signal that fires after object is saved, post saved signal when user is created
from django.db.models.signals import post_save 
# The sender 
from django.contrib.auth.models import User
# The receiver
from django.dispatch import receiver
# Profile from models
from .models import Profile

# Create profile function, run this everytime user is created
# When a user is saved, send this signal, signal then received by receiver
# create profile function takes all arguments, if user is created, then create profile object, with user equal to instance
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

# Function to save profile
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
	instance.profile.save()


