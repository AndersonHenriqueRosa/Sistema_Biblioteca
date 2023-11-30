from django.contrib import admin
from . models import Books, Genres

# Register your models here.
admin.site.register(Books)
admin.site.register(Genres)
