from django.db import models
from circular_feed.models import Circular

# Create your models here.
class Compose(models.Model):
    author = models.CharField(max_length=60)
    receiver = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    circular_id = models.ForeignKey('circular_feed.Circular', on_delete=models.CASCADE)