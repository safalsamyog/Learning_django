from django.urls import path
from . import views
urlpatterns = [
    path('web1/',views.fun1),
    path('web2/',views.fun2),
]