from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hlw(request):
	return HttpResponse("<h1>I am not a smart guy</h1>")
	
