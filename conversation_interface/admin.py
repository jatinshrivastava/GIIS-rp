from django.contrib import admin
from django.db import models
from conversation_interface.models import Message, MessageStatus

class MessageStatusAdmin(admin.ModelAdmin):
    list_display = ['circular_id', 'created_by','created_on','last_message_time','status']
    
    pass

class MessageAdmin(admin.ModelAdmin):
    list_display = ['circular_id','created_by','created_for','created_by_staff_username','created_on']
    
    pass

admin.site.register(Message, MessageAdmin)
admin.site.register(MessageStatus, MessageStatusAdmin)
