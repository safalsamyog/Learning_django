from django.urls import path
from . import views
urlpatterns = [
    path('2/',views.fun1),
    path('3/',views.fun_2),
    path('4/',views.fun_3),
    

]
