from django.urls import path
from conversation_interface import views

urlpatterns = [
    path('', views.conversation_index, name='conversation_index'),
]