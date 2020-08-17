'''from django.db import models
from Users.models import Users

# Create your models here.
class Score(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE,primary_key=True)
    score=models.IntegerField(max_length=5)'''
