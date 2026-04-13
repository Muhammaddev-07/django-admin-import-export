from django.db import models

# Create your models here.


class Phone(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField(blank=True,null=True)
    price= models.DecimalField(max_digits=10,decimal_places=2,default=0)
    brand=models.CharField(max_length=50, blank=True,null=True)