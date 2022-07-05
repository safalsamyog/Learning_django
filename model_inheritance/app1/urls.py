from django.urls import path

from . import views

urlpatterns=[
	path('student/',views.fun1),
	path('teacher/',views.fun2),
	path('',views.fun3),
	
]