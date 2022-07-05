from django import forms
from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields='__all__'

		#This is used for displaying all models fields in the form 

