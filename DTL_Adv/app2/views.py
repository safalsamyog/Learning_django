from django.shortcuts import render

# Create your views here.

def if_tag(request):
	val=None
	name='safal'
	bol=True
	age=90
	data={'val':val,'name':name,'bool':bol,'age':19}
	return render(request,'app2/index.html',data)

def for_tag(request):
	name=['safal','nischal','sulav','siddanta','sital']
	data={'name':name}
	return render(request,'app2/index2.html',data)
# This is the complex data where we are going to display
def for_tag_complx(request):
	stu={'stu1':{'name':'safal','class':11},
		 'stu2':{'name':'samyog','class':11},
		 'stu3':{'name':'nischal','class':11},
		 'stu4':{'name':'sital','class':11},

	}
	students={'student':stu}
	return render(request,'app2/index3.html',students)

def for_tag_7(request):
	data={'name':'samyog','class':11,'gender':'male'}

	return render(request,'app2/index4.html',{'data':data})

