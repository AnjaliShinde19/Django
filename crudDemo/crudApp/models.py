from django.db import models

# Create your models here.
class Student(models.Model):
    SNo = models.IntegerField()
    SName = models.CharField(max_length=30)
    SClass = models.IntegerField()
    SAddress = models.CharField(max_length=100)
    
