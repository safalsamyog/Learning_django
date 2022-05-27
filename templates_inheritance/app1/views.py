from django.shortcuts import render

# Create your views here.
def fun1(request):
	return render(request,'app1/index.html')

def fun_2(request):
	return render(request,'app1/base.html')

def fun_3(request):
	return render(request,'app1/home.html')

