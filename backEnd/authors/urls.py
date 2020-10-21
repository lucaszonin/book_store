from django.urls import path

from authors.views import (
    get_authors_view,
)

app_name = 'authors'

urlpatterns = [
    path('<slug>/', get_authors_view, name="detail"),
]