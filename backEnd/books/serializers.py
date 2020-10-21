from rest_framework import serializers

from books.models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta: 

        model = Book
        #fields = ['name', 'number_pages', 'year', 'updated_at']
        fields = ['name',
                  'img',
                  'cost_price',
                  'author', 
                  'category', 
                  'number_pages', 
                  'year', 
                  'updated_at', 
                  'created_at'
                  ]