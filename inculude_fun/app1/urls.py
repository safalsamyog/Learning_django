
from django.urls import path
from . import views
urlpatterns = [
    path('response1/',views.fun1),
    path('response2/',views.fun2),
]
