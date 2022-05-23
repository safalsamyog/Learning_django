from django.shortcuts import render

# Create your views here.
def fun1(request):
	return render(request,'index.html')

def fun2(request):
	return render(request,'index2.html')


