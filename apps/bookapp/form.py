from django.forms import *

from apps.bookapp.models import BookSearchModel, BookModel


class BookSearchForm(ModelForm):

    class Meta:
        model = BookSearchModel
        fields = ['name_of_book']

        widgets = {
            'name_of_book':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nombre del libro'
            })
        }


class RegisterForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class']='form-control'
            form.field.widget.attrs['autocomplete']='off'
        self.fields['cover_image'].widget.attrs['class']='form-control'

    class Meta:
        model = BookModel
        fields = [
            'title',
            'cover_image',
            'author',
            'summary',
            'category',
            'pdf',
            'backend_books',
            'frontend_books',
            'datascience_books',
        ]