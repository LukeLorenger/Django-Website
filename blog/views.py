from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView 
)
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
	# Dictionary
	context = { 
		'posts': Post.objects.all() # 
	}
	return render(request, 'blog/home.html', context)

# new class for class based views
class PostListView(ListView):
	model = Post
	# <app>/<model>_<viewtype>.html
	template_name = 'blog/home.html' 
	# attribute
	context_object_name = 'posts' 
	# Will order posts from newest to oldest
	ordering = ['-date_posted']
	# give us pagination functionality
	paginate_by = 2


class PostDetailView(DetailView):
	model = Post

# View with a form where we create a new post
# Passing in LoginRequiredMixin requires you to log in to create post
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content'] # set fields we want in form

	# override form valid method
	def form_valid(self, form):
		# before u submit form, take instance, set author to current logged in user
		form.instance.author = self.request.user 
		# validate form, Running form_valid method on parent class
		return super().form_valid(form) 

# Same as PostCreateView
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content'] 
	
	def form_valid(self, form):		
		form.instance.author = self.request.user 
		return super().form_valid(form) 

	# Runs test to make sure user editing post is author
	def test_func(self):
		# will get post we are currently trying to update
		post = self.get_object() 
		# check is current user is author of post
		if self.request.user == post.author:
			return True
		# If the user is not author, if conditional is not met,...False
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	# Once you delete post by clicking submit button, it will take you back to home page
	success_url = "/"

	def test_func(self):
		# will get post we are currently trying to update
		post = self.get_object() 
		# check is current user is author of post
		if self.request.user == post.author:
			return True
		# If the user is not author, if conditional is not met,...False
		return False


# About view function, Handles logic for about page, taking in request arguements
# Returning what we want the user to see when they are sent to this route
# Still returns HttpsResponse in background/This is passing info into our html.template
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

	# Notes
