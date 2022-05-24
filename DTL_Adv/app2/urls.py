from django.urls import path
from . import views
urlpatterns = [
    path('if/',views.if_tag),
    path('for/',views.for_tag),
    path('for2/',views.for_tag_complx),
    path('for3/',views.for_tag_7),

]