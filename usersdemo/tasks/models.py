from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Task(models.Model):
    name= models.CharField(max_length=30)
    description= models.TextField(blank=True)
    date= models.DateTimeField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("app_user:login",)
    