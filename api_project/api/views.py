from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Books to be viewed or edited.

    Authentication:
    - TokenAuthentication: Clients must provide a token in the Authorization header.
      Example: Authorization: Token <your-token-here>

    Permissions:
    - IsAuthenticated: Only logged-in users can access this API.
    - Can be customized per view or per action (e.g., admin-only for some operations)
    
    Usage:
    - GET /books_all/        → List all books (requires authentication)
    - POST /books_all/       → Create a new book (requires authentication)
    - PUT/PATCH /books_all/<id>/ → Update a book (requires authentication)
    - DELETE /books_all/<id>/ → Delete a book (requires authentication)

    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] # Only logged-in users can access
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Create your views here.
