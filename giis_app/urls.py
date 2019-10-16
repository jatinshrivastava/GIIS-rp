from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path("", include("circular_feed.urls")),
    path("conversation/", include("conversation_interface.urls")),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
]
