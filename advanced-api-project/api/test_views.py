from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def test_create_book(self):
        
        url = reverse('book-create')
        data = {
            "title":"mybook",
            "author":"abood",
            "publication_year":2025
        }

        response = self.client.post(url, data, format= 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)   
        book = Book.objects.get()
        self.assertEqual(book.title, "mybook")
        self.assertEqual(response.data["publication_year"], 2025)