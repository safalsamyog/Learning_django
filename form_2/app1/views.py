from django.shortcuts import render
from .forms import Form_dat
# Create your views here.
def fun1(request):
	#form=Form_dat(auto_id='some_%s')
	# form=Form_dat(auto_id=True)
	# form=Form_dat(auto_id=False)
	# form=Form_dat(auto_id='safal')
	#if we put any character then also it will think that it is true 
	# form=Form_dat(auto_id=True,label_suffix='')
	form=Form_dat(auto_id=True,label_suffix='-',initial={'name':'Samyog','email':'safal@gmail.com'})
	#label_suffix is used to edit last colon or anuthing

	#for ordering the field
	form.order_fields(field_order=['name','Address_name','email'])
	return render(request,'app1/index.html',{'form':form})