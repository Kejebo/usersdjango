from django.db import models
from django.urls import reverse
from django.conf import settings
class Task(models.Model):
    
    name=models.CharField(max_length=20)
    description=models.TextField(blank=True)
    date=models.DateField(auto_now=False, auto_now_add=False)
    employee=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.user.username
    
    
    