from django.urls import path
from . import views

urlpatterns = [
    path("", views.circular_index, name="circular_index"),
    path("<int:pcircular>/", views.circular_detail, name="circular_detail"),
  ]