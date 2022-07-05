from django.shortcuts import render
from .forms import StudentForm,TeacherForm,ExtForm
# Create your views here.

def fun1(request):
	if request.method=='POST':

		form=StudentForm(request.POST)

		if form.is_valid():
			form.save()
	else:
		form=StudentForm()
	return render(request,'app1/index.html',{'form':form})

def fun2(request):
	if request.method=='POST':

		form=TeacherForm(request.POST)

		if form.is_valid():
			form.save()#we can also save without cleaned datas
		
	else:
		form=TeacherForm()
	return render(request,'app1/index2.html',{'form':form})

def fun3(request):
	if request.method=='POST':

		form=ExtForm(request.POST)

		if form.is_valid():
			form.save()#we can also save without cleaned datas
		
	else:
		form=ExtForm()
	return render(request,'app1/index3.html',{'form':form})
