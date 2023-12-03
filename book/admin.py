from django.contrib import admin
from . models import Books, Genres,Lending

# Register your models here.
admin.site.register(Books)
admin.site.register(Genres)
admin.site.register(Lending)
