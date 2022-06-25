from django import forms

class Form_val(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()

	#Here we are going to made our own validation 
	# def clean_name of field(self):
	# 	valname=self.cleaned_data['name of field']

	def clean_name(self):
		valname=self.cleaned_data['name']

		#If condtion is True then it will run if false then it will not run
		if len(valname)<4:
			raise forms.ValidationError('Try to enter more than 4 chracter')
		return valname
	def clean_email(self):
		mail=self.cleaned_data['email']

		if mail=='sa@gmail.com':
			raise forms.ValidationError('You cant use this mail')
		return mail
