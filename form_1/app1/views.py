from django.shortcuts import render
from .forms import Dat_form
# Create your views here.

def form_1(request):
	form=Dat_form()
	return render(request,'app1/index.html',{'form':form})
