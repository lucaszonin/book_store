from django.urls import path

from books.views import (
    
    all_books_view,
    get_books_view,
    delete_books_view,
    update_books_view,
    create_books_view
)

app_name = 'books'

urlpatterns = [
    path('', all_books_view, name="all"),
    path('<slug>/', get_books_view, name="detail"),
    path('<slug>/delete', delete_books_view, name="delete"),
    path('<slug>/update', update_books_view, name="update"),
    path('create', create_books_view, name="create"),
]