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
    literary_genres = models.ForeignKey(Genres, on_delete=models.DO_NOTHING, blank=True)
    number_page = models.IntegerField()
    quantity_book = models.IntegerField()
    cover = models.ImageField(upload_to="book_images/", null=True, blank=True)
    publication_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    in_stock = models.BooleanField(default= False)

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Book'
    
class Lending(models.Model):
    user_lend = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    book_lend = models.ForeignKey(Books, on_delete=models.CASCADE, blank=True)
    date_Lend = models.DateField(auto_now_add=True)
    # date_return = models.DateField()

    def __str__(self):
        return f'{self.book_lend} | {self.user_lend}'
    
    class Meta:
        verbose_name = 'Lending'