from django import forms

class Form_1(forms.Form):
	Id=forms.IntegerField()
	name=forms.CharField(widget=forms.Textarea(attrs={'class':'name1','id':'id1'}))
	address=forms.CharField(widget=forms.CheckboxInput)
	file=forms.CharField(widget=forms.FileInput)
	email=forms.EmailField()
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'pass'}))
	none=forms.CharField(widget=forms.HiddenInput)
	url=forms.URLField(initial='https://facebook.com')
	#day = forms.DateField(initial=datetime.date.today)



#By using the attrs we can change the class name and id name to apply the css
