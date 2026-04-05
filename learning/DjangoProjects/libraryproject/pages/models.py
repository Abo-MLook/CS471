from django.db import models

# Create your models here.






#one to one
class Female (models.Model):
    name = models.CharField(max_length=50 , null = True)

    def __str__(self):
        return self.name

class Male(models.Model):
    name = models.CharField(max_length=50 , null = True)
    girls = models.OneToOneField(Female, on_delete=models.CASCADE)
    

   

    def __str__(self):
        return self.name


# one to many
class Product (models.Model):
    name = models.CharField(max_length=50 , null = True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50 , null = True)
    products = models.ForeignKey( Product , on_delete=models.CASCADE)
    

   

    def __str__(self):
        return self.name
    
    
    #===============
    
# many to many
class Video (models.Model):
    name = models.CharField(max_length=50 , null = True)

    def __str__(self):
        return self.name

class Watcher(models.Model):
    name = models.CharField(max_length=50 , null = True)
    products = models.ManyToManyField(Video , null = True)
    

   

    def __str__(self):
        return self.name
    
        