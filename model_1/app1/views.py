from django.shortcuts import render
from app1.models import Data
# Create your views here.

def fun1(request):
    data=Data.objects.all()
    return render(request,'app1/index.html',{'data':data})
