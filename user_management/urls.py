# my_project/urls.py
from django.contrib import admin
from django.urls import path, include # new
from django.views.generic.base import TemplateView

urlpatterns = [
  path("", views.circular_index, name="home"),
]