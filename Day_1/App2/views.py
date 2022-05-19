from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def App2(request):
	return HttpResponse("<h1>Hello! My name is Safal</h1>")
