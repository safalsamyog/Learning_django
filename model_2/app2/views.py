from django.shortcuts import render
from app2.models import Biodata
# Create your views here.
def fun2(request):
    data2=Biodata.objects.all()
    return render(request,'app2/index2.html',{'data':data2})