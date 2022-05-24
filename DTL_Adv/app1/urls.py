from django.urls import path
from . import views
urlpatterns = [
    path('',views.fun1),
    path('filter/',views.filter1),
    path('date_time/',views.date_time_filter),
    path('float/',views.Float_Format_Filter),
]
