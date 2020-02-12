from django.shortcuts import render
from django.views.generic import ListView # Importing ListView
from .models import Post # the . in fron of models means from model file in current package

# Self note, it is a good thing to pass the URL around in this manner
# We have a home page that gathers all post objects, passes them to home.html
# Helps with future production and routing purposes for steering users to proper location
# https://youtu.be/a48xeeo5Vnk?t=919 explains routing of URLs
# blog -> templates ->blog ->template.html


# Home view function, handling traffic from homepage, taking in requests arguements
# Returning what we want the user to see when they are sent to this route
# Still returns HttpsResponse in background/This is passing info into our html.template
def home(request):
	context = { # Dictionary
		'posts': Post.objects.all() # 
	}
	return render(request, 'blog/home.html', context)

# new class for class based views
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts' # attribute
	ordering = ['-date_posted']# Will order posts from newest to oldest

# About view function, Handles logic for about page, taking in request arguements
# Returning what we want the user to see when they are sent to this route
# Still returns HttpsResponse in background/This is passing info into our html.template
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

	# Notes
