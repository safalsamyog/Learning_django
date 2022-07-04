from django.shortcuts import render

# Create your views here.
def func1(request,x,name,idd,check):
	print(name,idd)
	return render(request,'app2/index.html',{'val':x})


def func2(request,xx=12):
	
	return render(request,'app2/index2.html')

