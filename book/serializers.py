from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'book_name': {'required': False},
            'author_name': {'required': False},
            'publisher_name': {'required': False},
            'book_image': {'required': False},
            'description': {'required': False},
            'language': {'required': False},
            'category': {'required': False},
            'book_type': {'required': False},
            'price': {'required': False},
            'available_for': {'required': False}
        }

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    message = serializers.CharField()
