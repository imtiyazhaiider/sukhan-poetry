from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

        widgets = {

            'username': forms.TextInput(
                attrs={
                    'class': 'w-full border rounded-xl p-3'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'w-full border rounded-xl p-3'
                }
            ),
        }