from django.db import models


# Create your models here.
class Question(models.Model):
    Question=models.CharField(max_length=500,unique=True)
    Option_A=models.CharField(max_length=200)
    Option_B=models.CharField(max_length=200)
    Option_C=models.CharField(max_length=200)
    Option_D=models.CharField(max_length=200)
    Answers=models.CharField(max_length=200)

