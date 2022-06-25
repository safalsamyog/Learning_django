from django.shortcuts import render
from .forms import Form_val
# Create your views here.
def fun1(request):
	if request.method=='POST':
		form=Form_val(request.POST)
		if form.is_valid():
			name=form.cleaned_data.get('name')
			
			email=form.cleaned_data.get('email')
			password=form.cleaned_data.get('password')
			print(name,email,password)

	else:
		form=Form_val()
	return render(request,'app1/index.html',{'form':form})
	