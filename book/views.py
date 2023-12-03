from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Books,Lending,Genres
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name="login")
def index(request):
    books = Books.objects.all()
    return render(request, "book/index.html", {"books": books})

def add_books(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST["author"]
        summary = request.POST.get("summary")
        literary_genres = request.POST["literary_genres"]
        number_page = request.POST["number_page"]
        quantity_book = request.POST["quantity_book"]
        cover = request.FILES.get("cover")
        publication_date = request.POST.get("publication_date")
        created_at  = datetime.now()

        if (
            not title
            or not author
            or not literary_genres
            or not quantity_book
        ):
            messages.error(request, "Por favor, preencha todos os campos.")
            return redirect("add-books")

        try:
            number_page = int(number_page)
            quantity_book = int(quantity_book)
        except ValueError:
            messages.error(
                request, "As páginas e a quantidade devem ser números inteiros."
            )
            return redirect("add-books")

        in_stock = True
        
        if int(quantity_book) == 0:
            in_stock = False

        Books.objects.create(
            title=title,
            author=author,
            summary=summary,
            literary_genres_id=literary_genres,
            number_page=number_page,
            quantity_book=quantity_book,
            cover=cover,
            publication_date=publication_date,
            created_at=created_at,
            in_stock=in_stock
        )

        messages.success(request, "Livro adicionado com sucesso!")
        return redirect("add-books")
    else:
        literary_genres = Genres.objects.all()
        return render(request, "book/add_book.html", {"literary_genres": literary_genres})

def book_detail(request, id):
    book = Books.objects.get(id=id)
    return render(request, "book/book_detail.html", {"book": book})


def book_Lending(request, id):
    book = Books.objects.get(id=id)
    user = request.user
    book.quantity_book -= 1
    book.save()
    lending= Lending.objects.create(book_lend=book, user_lend=user)   
    return render(request, "book/renew_lending.html", {"book": book, "lending": lending})
