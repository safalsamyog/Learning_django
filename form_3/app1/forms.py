from django import forms

class Form_Dat(forms.Form):
	name=forms.CharField(initial='Safal',help_text='it support 30 chars')#initial used to append data in input form
	# email=forms.EmailField()
	# address=forms.CharField()

class Fm(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
	address=forms.CharField()
	password=forms.CharField(widget=forms.HiddenInput())#This widget wll hide the input but not the key so overcome this problem lets write a code


