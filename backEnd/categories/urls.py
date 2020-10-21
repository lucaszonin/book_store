from django.urls import path

from categories.views import (
    get_categories_view,
)

app_name = 'categories'

urlpatterns = [
    path('<slug>/', get_categories_view, name="detail"),
    #path('<slug>/delete', delete_books_view, name="delete"),
]