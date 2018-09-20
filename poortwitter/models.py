from django.db import models


# Create your models here.
class Twitter(models.Model):
    tweet = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
