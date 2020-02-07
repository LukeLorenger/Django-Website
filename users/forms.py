from django import forms # importing forms from django
from django.contrib.auth.models import User # import user model
from django.contrib.auth.forms import UserCreationForm # import user creation form

# new class/form that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()# adding fields

	# Gives us a nest of namespace for configurations, keeps configs in one place
	class Meta:
		model = User # model to be affected
		fields = ['username', 'email', 'password1', 'password2'] # fields that we want in the form, and in what order


# Completed form that inherits from UserCreationForm
