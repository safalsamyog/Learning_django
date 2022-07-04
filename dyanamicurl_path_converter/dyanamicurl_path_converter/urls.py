"""dyanamicurl_path_converter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views

from app2 import views as vs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fun1/<int:x>/',views.fun1,name='fun1'),#if nothing there then it means str or anything
    path('',include('app1.urls')),
    path('',views.fun5,name='fun5'),
    path('Student/<int:grade>/<int:Id>/',views.fun6,name='fun6'),
    path('r/<int:b>/',views.fun7,{'check':'ok'},name='fun7'),
    path('page1/<int:x>',vs.func1,{'name':'samyog','idd':12,'check':'ok'},name='func1'),
    path('page2/<int:xx>/',vs.func2,name='func2')
]
