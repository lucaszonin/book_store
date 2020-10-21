from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from authors.models import Author
from authors.serializers import AuthorSerializer

# Create your views here.

@api_view(['GET',])
def get_authors_view(request, slug):

    try:
        author = Author.objects.get(slug=slug)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":

        serializer = AuthorSerializer(author)
        return Response(serializer.data)


# @api_view(['DELETE',])
# def delete_books_view(request, slug):

#     try:
#         book = Book.objects.get(slug=slug)
#     except Book.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "DELETE":
        
#         operation = book.delete()
#         data = {}
#         if operation:
#             data['success'] = 'book deleted with success'
#         else:
#             data['failure'] = 'delete failed'
            
#         return Response(data=data)


    