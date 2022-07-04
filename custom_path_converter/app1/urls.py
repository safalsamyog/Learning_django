from django.urls import path,register_converter

from . import views,converters

register_converter(converters.FourYearDigitConverter,'yyyy')
urlpatterns=[
	path('session/<yyyy:year>/',views.fun1,name='fun1'),
]