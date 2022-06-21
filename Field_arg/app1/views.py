from django.shortcuts import render
from .forms import Form_1
# Create your views here.
def fun1(request):
	form=Form_1(initial={'email':'ur email'})#wrting here is more piroty
	form.order_fields(field_order=['name','address','email'])
	return render(request,'app1/index.html',{'form':form})