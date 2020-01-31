from django.shortcuts import render
from django.http import HttpResponse

# Home function, handling traffic from homepage, taking in requests arguements
# Returning what we want the user to see when they are sent to this route
def home(request):
	return HttpResponse('<h1>Blog Home Cunts!</h1>')
	# 5. Home function, now it will return HttpResponse

# About function, Handles logic for about page, taking in request arguements
def about(request):
	return HttpResponse('<h1>Blog About Cunty biscuits!</h1>')

def selftest(request):
	return HttpResponse('<h1>Blog selftest Cunty biscuits...DRY!</h1>')