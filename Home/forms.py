from django import forms
from .models import Book, Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "age","alive"]
        labels = {
            "name": "نام نویسنده",
            "age": "سن",
            "alive":"زنده است؟"
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "author"]
        labels = {
            "title": "عنوان کتاب",
            "description": "توضیحات",
            "author": "نویسنده",
        }