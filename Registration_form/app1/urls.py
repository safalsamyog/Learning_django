from django.urls import path
from . import views

urlpatterns=[
    path('SignUp/',views.Sign_Up),
    path('',views.Sign_Up_more)
]