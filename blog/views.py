from django.shortcuts import render

# Self note, it is a good thing to pass the URL around in this manner
# Helps with future production and routing purposes for steering users to proper location
# https://youtu.be/a48xeeo5Vnk?t=919 explains routing of URLs
# blog -> templates ->blog ->template.html

# Passable "posts", using as dummy data, this is a list of dictionaries
posts = [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'January 30, 2020'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'January 30, 2020'
	}
]

# Home function, handling traffic from homepage, taking in requests arguements
# Returning what we want the user to see when they are sent to this route
# Still returns HttpsResponse in background/This is passing info into our html.template
def home(request):
	context = { # Dictionary
		'posts': posts # Key, makes dummy data accessible from within home.html template
	}
	return render(request, 'blog/home.html', context)

# About function, Handles logic for about page, taking in request arguements
# Returning what we want the user to see when they are sent to this route
# Still returns HttpsResponse in background/This is passing info into our html.template
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
