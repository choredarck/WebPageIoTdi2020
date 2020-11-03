from django.db import models

# Create your models here.

class sensordata(models.Model):
    idd= models.IntegerField()
    valor= models.IntegerField()
    estado= models.CharField(max_length=30)
