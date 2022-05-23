
from django.urls import path
from . import views
urlpatterns = [
    path('response3/',views.fun3),
    path('response4/',views.fun4),
]
