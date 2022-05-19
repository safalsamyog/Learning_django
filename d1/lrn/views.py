from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_dj(request):
	return HttpResponse('<h1>hello I am learning Django</h1>')

def bio(request):
	a="and safal"
	return HttpResponse(f'<h2>My name is samyog bhattarai {a}</h2>')
