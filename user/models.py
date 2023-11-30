from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'User'
