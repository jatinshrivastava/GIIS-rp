from django.contrib import admin
from circular_feed.models import Circular

class CircularAdmin(admin.ModelAdmin):
    pass

admin.site.register(Circular, CircularAdmin)