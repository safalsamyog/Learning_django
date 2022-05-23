from django.urls import path
from . import views
urlpatterns = [
    path('f1/',views.func1),
    path('f2/',views.func2),
]
