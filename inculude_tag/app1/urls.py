from django.urls import path
from . import views
urlpatterns = [
    path('1/',views.fun1,name='1'),
    path('2/',views.fun2,name='2'),
    path('3/',views.fun3,name='3'),
]
