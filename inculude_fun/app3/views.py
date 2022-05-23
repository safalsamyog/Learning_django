from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def func5(request):
	return HttpResponse("<h1>Hello django</h1>")

	
