import csv

from django.db import models
from django.db import IntegrityError
from Role.models import Role

# Create your models here.

class Users(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Username=models.CharField(max_length=100,unique=True)
    Email_Id=models.EmailField(max_length=250)
    Password=models.CharField(max_length=50)
    Roles=models.ForeignKey(Role,on_delete=models.CASCADE)

