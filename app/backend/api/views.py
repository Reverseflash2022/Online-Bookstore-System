from rest_framework import generics
from ..models import Book, Author, Genre, Order, Review
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, OrderSerializer, ReviewSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Similar views for Author, Genre, Order, Review
