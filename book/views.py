from django.shortcuts import render, redirect
from user.models import Users
from . models import Books
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name="login")
def index(request):
    books = Books.objects.all()
    print(f"book.name ")
    return render(request, "book/index.html", {"books": books})

def books_detail(request, id):
    books = Books.objects.get(id=id)
    return render(request, "book/books_detail.html", {"books": books})