from django.shortcuts import render

# Create your views here.
def fun1(request):
	name="Safal"
	class_=12
	roll=15
	data_={'name':name,'class_':class_,'roll':roll}
	return render(request,'app1/index.html',context=data_)