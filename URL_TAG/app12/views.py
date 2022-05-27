from django.shortcuts import render

# Create your views here.
def fun_1(request):
	return render(request,'app12/index.html')

def fun_2(request):
	return render(request,'app12/index2.html')

