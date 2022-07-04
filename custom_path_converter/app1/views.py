from django.shortcuts import render

# Create your views here.

def fun1(request,year):
	return render(request,'app1/index.html',{'val':year})


# def fun2(request):
# 	return render(request,'app1/index.html',{'':})