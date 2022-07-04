from django.urls import path

from . import views

urlpatterns=[
    path('fun2/<str:myname>/',views.fun2,name='fun2'),
    path('fun3/<int:num>/',views.fun3,name='fun3'),
    path('fun4/<slug:slg>/',views.fun4,name='fun4'),
]