from django.db import models

# Create your models here.

class registration(models.Model):
 
 name= models.CharField(max_length=121)
 email=models.CharField(max_length=120)
 location = models.CharField(max_length=100)
 mobile = models.CharField(max_length=12)
 date = models.DateField()
