from django import forms

class Form_dat(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
	Address_name=forms.CharField()
	#as _ underscore work as a space as seen in html just like Address name

