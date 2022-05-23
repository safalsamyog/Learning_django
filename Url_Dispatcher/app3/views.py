from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fun(request):
	a="<h1>Hello i am learning django<h2>"
	return HttpResponse(a)


