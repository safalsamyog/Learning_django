import re
from django.shortcuts import render
from app1.models import Std_data
# Create your views here.
def fun1(request):
    data=Std_data.objects.all()

    return render(request,'app1/index.html',{'datas':data})