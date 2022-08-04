from django.urls import path
from . import views

urlpatterns=[
    path('SignUp/',views.SignUp,name='signup'),
    path('login/',views.log_in,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.log_out,name='logout')
]