from django import forms

#Learning Forms field detailly
class Dat_form(forms.Form):
	name=forms.CharField(min_length=5,max_length=10,error_messages={'required':'Enter ur name here'},strip=False,empty_value='Samyog')
	email=forms.EmailField(max_length=70,error_messages={'required':'Email hala ramrosanga'})
	check=forms.BooleanField(required=False)
	Id=forms.IntegerField(min_value=1,max_value=100)
	dec=forms.DecimalField(min_value=0,max_value=1000,max_digits=5,decimal_places=1)
	float_1=forms.FloatField(min_value=0,max_value=1000)
	url=forms.URLField()
	slg=forms.SlugField()
	txt=forms.CharField(max_length=50,widget=forms.Textarea(attrs={'rows':7,'cols':16}))
	inp=forms.FileField()
	img=forms.ImageField()

#To avoid the space we use strip=True if no then False
#empty_value just passing but will not appear in form and its dont get tageted by validation but can be sent to form
#Boolean field shows check box if empty then it return false