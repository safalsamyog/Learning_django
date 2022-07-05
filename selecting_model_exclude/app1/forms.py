from django import forms
from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		exclude=['address']#Except this field all field will display on the form

		#This is used for displaying all models fields in the form 

