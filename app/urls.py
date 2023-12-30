from django.urls import re_path as url
from . import views


urlpatterns = [
    url(r'search/', views.search),
    url(r'info/', views.info)
]
