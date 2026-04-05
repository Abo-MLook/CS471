from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    content = models.TextField(null=True,blank=True, verbose_name='explantion') # all about null , blank and verbose name
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    
    catgs = [
        ('CS','CS'),
        ('IT','IT')
    ]
    category = models.CharField(null=True,blank=True,choices=catgs)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Teacher'
        ordering = ['-price'] #- decending
        
        
from datetime import datetime  
from django.utils import timezone

class History(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    history = models.DateTimeField(default = timezone.now)