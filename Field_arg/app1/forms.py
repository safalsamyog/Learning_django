from django import forms

class Form_1(forms.Form):
	name=forms.CharField(label='Yourname',label_suffix='-',initial='Name field',help_text='plz enter ur name here')
	email=forms.EmailField(label='E-mail',label_suffix='::',initial='Email field',required=False,help_text='Enter email here')
	address=forms.CharField(disabled=True)



#label is used to change the name of field which is displayed on fronted
#label_suffix is used to edit last colon of label which we can chnage by any symbol and alphabet only
#initial is used to render value in field input 
#required is already deafult so we can change
#disabled used to disable input field and we cant input there any value
#help_text is used to show some information and we can do css which is build with span and class name with helptext
