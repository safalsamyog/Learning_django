from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fun3(request):
	return HttpResponse("300")

def fun4(request):
	return HttpResponse("700")



