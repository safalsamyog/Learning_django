from django.shortcuts import render
from .forms import Form_Dat,Fm
# Create your views here.
def fun1(request):
	form=Form_Dat(auto_id=True,label_suffix=': ')
	
	return render(request,'app1/index.html',{'form':form})

def fun2(request):
	form=Fm(auto_id=True,label_suffix=': ')
	form.order_fields(field_order=['name','address','email'])
	return render(request,'app1/index2.html',{'form':form})
