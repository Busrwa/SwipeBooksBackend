from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, NumberFilter
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .permissions import IsTeamLeadOrAdmin


class BookPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookFilter(FilterSet):
    search = CharFilter(method='filter_search', label='Search')
    author_id = NumberFilter(field_name='author__id')
    isbn = CharFilter(field_name='isbn', lookup_expr='icontains')

    def filter_search(self, queryset, name, value):
        from django.db.models import Q
        return queryset.filter(
            Q(title__icontains=value) |
            Q(author__name__icontains=value) |
            Q(isbn__icontains=value)
        )

    class Meta:
        model = Book
        fields = ['author_id', 'isbn']


# --- AUTHOR ---
class AuthorListCreateView(APIView):
    permission_classes = [IsTeamLeadOrAdmin]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.check_permissions(request)
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailView(APIView):
    permission_classes = [IsTeamLeadOrAdmin]

    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        self.check_permissions(request)
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.check_permissions(request)
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- BOOK ---
class BookListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsTeamLeadOrAdmin]
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ['id', 'title', 'publish_date']
    ordering = ['id']

    def get_queryset(self):
        return Book.objects.select_related('author').all()


class BookDetailView(APIView):
    permission_classes = [IsTeamLeadOrAdmin]

    def get(self, request, pk):
        book = get_object_or_404(Book.objects.select_related('author'), pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        self.check_permissions(request)
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.check_permissions(request)
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
