from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        #fields = ('book_user', 'id', 'name', 'author', 'edition', 'publisher', 'issue_date')
        fields = '__all__'

