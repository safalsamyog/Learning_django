from django import forms

class Dat_form(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
