from django import forms

class Form_val(forms.Form):
	error_css_class='err'
	required_css_class='required'
	name=forms.CharField(error_messages={'required':'Dont leave empty u bastard'},min_length=4)
	email=forms.EmailField(error_messages={'required':'Dont leave email u baka'},min_length=6)

