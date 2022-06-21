from django.shortcuts import render
from .forms import Form_1
# Create your views here.
def fun1(request):
	form=Form_1()
	
	return render(request,'app1/index.html',{'form':form})