from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import *


class CreatUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username': TextInput(attrs={
                'placeholder':'Usuario'
            }),
            'email': EmailInput(attrs={
                'placeholder': 'Correo electrónico',
                'required':'true',
                'maxlength':'10',

            }),
            'password1': PasswordInput(attrs={
                'placeholder': 'Password'
            }),
            'password2': PasswordInput(attrs={
                'placeholder': 'Repetir Password'
            }),
        }