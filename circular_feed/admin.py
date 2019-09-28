from django.contrib import admin
from circular_feed.models import Circular
from conversation_interface.models import Compose

class CircularAdmin(admin.ModelAdmin):
    pass

admin.site.register(Circular, CircularAdmin)

class ComposeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Compose, ComposeAdmin)