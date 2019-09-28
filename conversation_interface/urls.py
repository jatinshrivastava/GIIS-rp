from django.urls import path
from conversation_interface import views

urlpatterns = [
    path("compose/<int:pk>/", views.compose, name='compose'),
]