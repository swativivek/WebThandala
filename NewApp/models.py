from django.db import models
from datetime import datetime
# Create your models here.
class usermsg(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    messg = models.TextField(blank =True)
    display = models.TextField(blank=True)

    def __str__(self):
        return self.Name