from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def App1(request):
	return HttpResponse("<h1>Hello! I am learning Django</h1>")

