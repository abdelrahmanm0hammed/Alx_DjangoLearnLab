from rest_framework import serializers
from datetime import datetime
from .models import Book , Author

# BookSerializer to convet data coming from python to JSON and vice versa 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(f"Publication year cannot be in the future (current year is {current_year}). ")
        return value # returning the validated value to keep it and continue processing
    
class AuthorSerializer(serializers.ModelSerializer):
    books =BookSerializer(many=True, read_only = True)
    class Meta:
        model = Author
        fields = ['name']

