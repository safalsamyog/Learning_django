from django.shortcuts import render
from datetime import datetime
# Create your views here.
def fun1(request):
	msg="Hello! How are you"
	name="samyog"
	class_=11
	
	data={"response":msg,"name":name,"class_":class_}

	return render(request,'app1/index.html',data)

def filter1(request):
	lower_val="kathmandu"
	upper_val="SAMYOG"
	bool1="Hello"
	bool2=False
	country='Nepal'
	data={'val1':lower_val,'val2':upper_val,'bool1':bool1,'bool2':bool2,'country':country}
	return render(request,'app1/index2.html',data)
#Learning Django Template Language

def date_time_filter(request):
	d=datetime.now()#we need to import datetime module to work in django template language
	return render(request,'app1/index3.html',{'Time':d})


#Function for float filters

def Float_Format_Filter(request):
	val1=123.345
	val2=723.000
	val3=777.0345
	float_data={'val1':val1,'val2':val2,'val3':val3}
	return render(request,'app1/index4.html',float_data)

