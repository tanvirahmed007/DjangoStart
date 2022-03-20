from django.db import models

# Create your models here.
class Feature(models.Model):
    
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=500)
    is_true: bool

class Myself(models.Model):
    name = models.CharField(max_length=50)
    sub = models.CharField(max_length=50)
    para = models.CharField(max_length=50)
