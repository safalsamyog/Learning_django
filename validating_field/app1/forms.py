from django import forms

class Form_val(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
	password=forms.CharField(widget=forms.PasswordInput)


	#Lets do validation custom in one function

	def clean(self):
		cleaned_data=super().clean()
		valname=self.cleaned_data['name']
		mail=self.cleaned_data['email']
		# password_1=self.cleaned_data['password']
	

		if len(valname) < 4 and '!' in valname or '@' in valname:
			raise forms.ValidationError('wrong')

		if len(mail) >13:
			raise forms.ValidationError('Wrong wrong')




