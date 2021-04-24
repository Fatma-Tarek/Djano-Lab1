from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view

@api_view(["GET"])
def index(request):
    books = Book.objects.all()
    serializer = BookSerializer(instance=books, many= True)
    return Response(data=serializer.data, status= status.HTTP_200_OK)