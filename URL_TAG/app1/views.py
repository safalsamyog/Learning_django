from django.shortcuts import render

# Create your views here.
def fun1(request):
	return render(request,'app1/index.html')

def fun2(request):
	return render(request,'app1/index2.html',{"abt":"/fun2"})
	