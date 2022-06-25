from django import forms
from django.core import validators

#Runnning Builtin Validation from pacakges


#Lets create custom Validators

def func(value):
	if value[0]=='s':
		raise forms.ValidationError('You cannot use s in starting plz')
def func2(value):
	if len(value)<3:
		raise forms.ValidationError('too low')
class Form_val(forms.Form):
	name=forms.CharField(validators=[validators.MaxLengthValidator(10)])
	email=forms.CharField(validators=[func,func2])#we can use more than one 
	password=forms.CharField(widget=forms.PasswordInput)






