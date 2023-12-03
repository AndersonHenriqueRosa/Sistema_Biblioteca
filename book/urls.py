from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('book_detail/<int:id>', views.book_detail, name='book-detail'),
    path('book_Lending/<int:id>', views.book_Lending, name='book_Lending'),
    path("add-books/", views.add_books, name="add-books"),
]