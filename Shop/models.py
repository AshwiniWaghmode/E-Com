from django.db import models

# Create your models here.

class Register(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.CharField(max_length=25)
    
    password=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.Name
    
