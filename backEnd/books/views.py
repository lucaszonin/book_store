from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from books.models import Book
from books.serializers import BookSerializer

# Create your views here.

@api_view(['GET',])
def all_books_view(request):

    book = Book.objects.all()

    if request.method == "GET":

        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def get_books_view(request, slug):

    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":

        serializer = BookSerializer(book)
        return Response(serializer.data)


@api_view(['DELETE',])
def delete_books_view(request, slug):

    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        
        operation = book.delete()
        data = {}
        if operation:
            data['success'] = 'book deleted with success'
        else:
            data['failure'] = 'delete failed'
            
        return Response(data=data)


@api_view(['PUT',])
def update_books_view(request, slug):

    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":

        serializer = BookSerializer(book, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "Book updated with success"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def create_books_view(request):
    #request.data['teste']

    #request.data['sell_price'] = calcular_valor_por_margem(request.data['margem'], request.data['cost_price'])

    if request.method == "POST":

        serializer = BookSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "Book created with success"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Calculando quanto vender o valor baseado no custo e na margem definida
# def calcular_valor_por_margem(margem, cost_price):
    
#     valor_venda_produto = (cost_price + (margem * cost_price) / 100)
#     return valor_venda_produto
