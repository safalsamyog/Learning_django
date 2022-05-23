from django.shortcuts import render

# Create your views here.
def fun2(request):
	return render(request,'app2/index2.html')
