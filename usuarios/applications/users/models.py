from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin ):
    GENDER_CHOICES =[
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros'),
    ]
    username=models.CharField(max_length=20, unique=True)
    email=models.EmailField(max_length=254)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    
    USERNAME_FIELD='username'
    objects= UserManager()
    def get_short_name(self):
        return self.username
    
    def __str__(self):
        return self.first_name+' '+self.last_name
    