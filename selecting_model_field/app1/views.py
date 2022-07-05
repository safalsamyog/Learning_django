from django.shortcuts import render
from .forms import UserForm
# Create your views here.

def fun1(request):
	if request.method=='POST':

		form=UserForm(request.POST)

		if form.is_valid():
			name=form.cleaned_data['name']
			email=form.cleaned_data['email']
	else:
		form=UserForm()
	return render(request,'app1/index.html',{'form':form})

