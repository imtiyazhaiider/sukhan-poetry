from django import forms

from .models import Draft


class DraftForm(forms.ModelForm):

    class Meta:

        model = Draft

        fields = [
            'title',
            'writing_type',
            'language',
            'content'
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'w-full border rounded-xl p-3'
                }
            ),

            'writing_type': forms.Select(
                attrs={
                    'class': 'w-full border rounded-xl p-3'
                }
            ),

            'language': forms.Select(
                attrs={
                    'class': 'w-full border rounded-xl p-3'
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'class': 'w-full border rounded-xl p-4',
                    'rows': 15,
                    'placeholder': 'Start writing your poetry...'
                }
            ),
        }