"""Day_2 URL Configuration

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
#Learning Url dispatcher
from django.contrib import admin
from django.urls import path
from app1 import views as a
from app2 import views as a1
from app3 import views as a2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',a.Name),
    path('greet/',a1.hlw),
    path('t/',a2.fun),
]
