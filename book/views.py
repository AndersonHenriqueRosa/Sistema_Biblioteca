from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import Users
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name="login")
def index(request):
    books = books.objects.filter(user_id=request.user.id).order_by("cod")

    for book in books:
        print(f"book.name ")
    return render(request, "book/index.html", {"books": books})
