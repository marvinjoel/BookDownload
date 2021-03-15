from django import forms

from apps.bookapp.models import BookSearchModel


class BookSearchForm(forms.ModelForm):

    class Meta:
        model = BookSearchModel
        fields = ['name_of_book']

        widgets = {
            'name_of_book':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nombre del libro'
            })
        }