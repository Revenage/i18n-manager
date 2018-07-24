from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from . import views

# urlpatterns = [
#     url(r'web', views.index, name='index'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
]
