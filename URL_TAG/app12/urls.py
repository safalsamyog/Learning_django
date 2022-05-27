from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.fun_1,name='11'),
    path('22/',views.fun_2,name='22'),
]
