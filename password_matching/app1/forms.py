from django import forms

class Form_val(forms.Form):
	name=forms.CharField(max_length=50,min_length=3,widget=forms.TextInput(attrs={'class':'f'}))
	email=forms.EmailField(max_length=50,widget=forms.TextInput(attrs={'class':'f'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'f'}))
	repassword=forms.CharField(widget=forms.PasswordInput)


	def clean(self):
		cleaned_data=super().clean()

		pass1=self.cleaned_data['password']
		pass2=self.cleaned_data['repassword']

		if pass1 != pass2:
			raise forms.ValidationError('password doesnot match')

