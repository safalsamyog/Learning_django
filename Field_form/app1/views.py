from django.shortcuts import render
from .forms import Dat_form
# Create your views here.

def form_1(request):
	if request.method=='POST':
		form=Dat_form(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			email=form.cleaned_data['email']
			check=form.cleaned_data['check']
			Id=form.cleaned_data['Id']
			dec=form.cleaned_data['dec']
			flt=form.cleaned_data['float_1']
			url=form.cleaned_data['url']
			slg=form.cleaned_data['slg']
			print(name)
			print(email)
			print(check)
			print(Id)
			print(dec)
			print(flt)
			print(url)
			print(slg)
	else:
		form=Dat_form()
	return render(request,'app1/index.html',{'form':form})
