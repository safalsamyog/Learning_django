from django.shortcuts import render

# Create your views here.
def fun2(request):
	name="samyog"
	class_=11
	roll=13
	data_={'name':name,'class_':class_,'roll':roll}
	return render(request,'app2/index2.html',context=data_)
	#or return render(request,'app1/index.html',data_)