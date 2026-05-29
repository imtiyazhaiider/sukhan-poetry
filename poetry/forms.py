from django import forms

from .models import Submission


class SubmissionForm(forms.ModelForm):

    class Meta:

        model = Submission

        fields = [
            'poet_name',
            'poet_biography',
            'title',
            'content',
            'writing_type',
            'language',
            'submitted_by',
        ]

        widgets = {

            'poet_name': forms.TextInput(
                attrs={
                    'class': 'w-full border rounded-xl p-3'
                }
            ),

            'poet_biography': forms.Textarea(
                attrs={
                    'class': 'w-full border rounded-xl p-3',
                    'rows': 4
                }
            ),

            'title': forms.TextInput(
                attrs={
                    'class': 'w-full border rounded-xl p-3'
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'class': 'w-full border rounded-xl p-3',
                    'rows': 10
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

            'submitted_by': forms.TextInput(
                attrs={
                    'class': 'w-full border rounded-xl p-3'
                }
            ),
        }