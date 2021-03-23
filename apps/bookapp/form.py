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
    pdf = CharField(widget=FileInput(attrs = {'type': 'file', 'accept': '.pdf', 'id': 'upload-pdf', 'style': 'display: none'}))
    cover_image = CharField(widget=FileInput(attrs={'type':'file','accept':'image/jpeg, image/png','id':'upload-front-pdf','style':'display: none'}))
    # category = CharField(widget=TextInput(attrs={'class':'custom-select','id':'category-pdf'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class']='form-control'
            form.field.widget.attrs['autocomplete']='off'
        self.fields['backend_books'].widget.attrs['class']='form-check-input'
        self.fields['frontend_books'].widget.attrs['class']='form-check-input'
        self.fields['datascience_books'].widget.attrs['class']='form-check-input'
        self.fields['title'].widget.attrs['placeholder']='Ejem: PHP, React, Python, Laravel'
        self.fields['author'].widget.attrs['placeholder']='Ejem: Mark Tielens Thomas'
        self.fields['summary'].widget.attrs['placeholder']='Una corta descripción del libro...'


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

        widgets = {
            'summary':Textarea(attrs={'rows':'3'}),
            # 'category':
            'backend_books':CheckboxInput(attrs={'id':'flexCheckDefault'}),
            'frontend_books':CheckboxInput(attrs={'id':'flexCheckChecked'}),
            'datascience_books':CheckboxInput(attrs={'id':'flexCheckCheckedes'}),
            'pdf': FileField(),
            'cover_image':ImageField(),
        }
        # attrs = {'type': 'file', 'accept': '.pdf', 'id': 'upload-pdf', 'style': 'display: none'}
# attrs={'type':'file','accept':'image/jpeg, image/png','id':'upload-front-pdf','style':'display: none'}
