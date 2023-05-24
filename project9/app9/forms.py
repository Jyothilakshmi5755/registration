from app9.models import Book
from django.forms import ModelForm

class bookForm(ModelForm):
    class Meta:
        model = Book
        fields='__all__'