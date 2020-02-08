from django.shortcuts import render, redirect
from django.contrib import messages # What type of message we would like to add
from django.contrib.auth.decorators import login_required # require a user is logged in to view the profile
from .forms import UserRegisterForm # importing the created UserRegisterForm with email field

# register view FUNCTION
def register(request):
	if request.method == 'POST': # If we get post request, we will validate form data
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save() # Save User
			username = form.cleaned_data.get('username') # If valid, grab username
			messages.success(request, f'Your account has been created! You are now able to login.') # Flashed message using F string
			return redirect('login') # name we gave to URL pattern for blog home page

	else: # if not, display blank form
		form = UserRegisterForm() # Instance of the form
	return render(request, 'users/register.html', {'form': form}) # render template that uses this form, uses instance

@login_required # Decorator, adds functionality to an existing function
def profile(request):
	return render(request, 'users/profile.html')




# The diff types of messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error


