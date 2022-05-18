from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['name', 'author', 'desc', 'price', 'book_image']
