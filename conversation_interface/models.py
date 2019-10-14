from django.db import models
from datetime import datetime

# Create your models here.
class Message(models.Model):
    created_by = models.CharField(max_length=20)
    created_for = models.CharField(max_length=20, default='staff')
    created_by_staff_username = models.CharField(max_length=20, default='admin')
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    circular_id = models.ForeignKey('circular_feed.Circular', on_delete=models.CASCADE)

class MessageStatus(models.Model):
    Open = 'Open'
    Waiting_for_acknowledgement = 'Waiting for response'
    Closed = 'Closed'
    
    Status_Choices = [
        (Open, 'Open'),
        (Waiting_for_acknowledgement, 'Waiting for response'),
        (Closed, 'Closed'),
    ]
    created_by = models.CharField(max_length=20)
    status = models.CharField(max_length=20,choices=Status_Choices,
        default=Open)
    last_message = models.TextField()
    last_message_time = models.DateTimeField(default=datetime.now)
    created_on = models.DateTimeField(auto_now_add=True)
    circular_id = models.ForeignKey('circular_feed.Circular', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('circular_id', 'created_by',)