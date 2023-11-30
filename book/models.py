from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genres(models.Model):
    name= models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Genre'
    
    
    

class Books(models.Model):
    title = models.CharField(max_length= 80) 
    author = models.CharField(max_length= 30)
    summary = models.TextField(blank= True)
    literary_genres = models.ForeignKey(Genres, on_delete=models.CASCADE, blank=True)
    number_page = models.IntegerField()
    quantity_book = models.IntegerField()
    cover = models.ImageField(upload_to="book-cover/", null=True, blank=True)
    publication_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    in_stock = models.BooleanField(default= False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Book'
    
