from django.shortcuts import render

# Create your views here.
def fun1(request):
	return render(request,'app1/index.html',{'d':'php'})

def fun2(request):
	return render(request,'app1/index2.html')


def fun3(request):
	return render(request,'app1/ext.html')