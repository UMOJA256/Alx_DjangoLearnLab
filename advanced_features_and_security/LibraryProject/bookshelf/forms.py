from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    Form for creating a new Book instance.
    Uses the Book model and all its fields.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'published_date': 'Published Date',
        }
