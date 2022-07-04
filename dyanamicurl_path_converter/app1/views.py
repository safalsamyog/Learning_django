from django.shortcuts import render

# Create your views here.
def fun1(request,x):
	

	if x==1:
		std={'myid':x,'name':'samyog'}
	elif x==2:
		std={'myid':x,'name':'safal'}
	elif x==3:
		std={'myid':x,'name':'sama'}
	elif x==4:
		std={'myid':x,'name':'tool'}
	elif x==5:
		std={'myid':x,'name':'nischal'}
	elif x==6:
		std={'myid':x,'name':'sital'}
	else:
		pass






	return render(request,'app1/index.html',std)


def fun2(request,myname):
	x=myname
	return render(request,'app1/index.html',{'myname':x})

def fun3(request,num):
	x=num
	return render(request,'app1/index.html',{'number':x})

def fun4(request,slg):
	x=slg
	return render(request,'app1/index.html',{'slug':x})

def fun5(request):

	return render(request,'app1/home.html',{'i':[1,2,3,4,5,6]})

def fun6(request,grade,Id):

	if grade==1 and Id==1:
		std={'myid':grade,'name':'samyog'}
	elif grade==2 and Id==2:
		std={'myid':grade,'name':'safal'}
	elif grade==3 and Id==3:
		std={'myid':x,'name':'sama'}
	elif grade==4 and Id==4:
		std={'myid':x,'name':'tool'}
	elif grade==5 and Id==5:
		std={'myid':grade,'name':'nischal'}
	elif grade==6 and Id==6:
		std={'myid':grade,'name':'sital'}
	else:
		pass






	return render(request,'app1/index.html',std)

def fun7(request,b,check):#we can give deafult argument here and also we can provide another value 
	print(check)
	return render(request,'app1/b.html',{'b':b})