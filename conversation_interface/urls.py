from django.urls import path
from . import views

urlpatterns = [
    path("index/<int:pcircular>", views.conversation_index, name="conversation_index"),
    path("index/<int:pcircular>/<slug:receiver>", views.staff_messages, name="staff_messages"),
    path("messages/<int:pcircular>/<slug:receiver>", views.messages, name="messages"),
    path("user_unauthorized/", views.unauthorized, name="unauthorized"),
  ]