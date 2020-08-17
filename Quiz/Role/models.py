import csv

from django.db import models,IntegrityError

# Create your models here.
class Role(models.Model):
    Role_Id=models.CharField(primary_key=True,max_length=5)
    Role_name=models.CharField(max_length=100,unique=True)



