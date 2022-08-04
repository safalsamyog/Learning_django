#from dataclasses import field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
class UForm(UserCreationForm):
	password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']
		labels={'email':'email'}
class User_Change(UserChangeForm):
	password=None
	class Meta:
		model=User
		fields=['first_name','last_name','email','date_joined','last_login']
		labels={'email':'email'}
    	

class Admin_Change(UserChangeForm):
	password=None
	class Meta:
		model=User
		fields='__all__'
		labels={'email':'email'}