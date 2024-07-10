from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer,PartialUpdateBookSerializer
from .pagination import CustomPageNumberPagination  

class BookFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre', lookup_expr='iexact')

    class Meta:
        model = Book
        fields = ['genre']

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    pagination_class = CustomPageNumberPagination  

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PartialUpdateBookSerializer
        return BookSerializer