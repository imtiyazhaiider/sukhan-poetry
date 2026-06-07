from django.db import models

from django.contrib.auth.models import User


class Draft(models.Model):

    WRITING_TYPES = [
        ('sher', 'Sher'),
        ('ghazal', 'Ghazal'),
        ('nazm', 'Nazm'),
        ('shayari', 'Shayari'),
        ('quote', 'Quote'),
    ]

    LANGUAGE_CHOICES = [
        ('urdu', 'Urdu'),
        ('hindi', 'Hindi'),
        ('english', 'English'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='drafts'
    )

    title = models.CharField(
        max_length=255
    )

    content = models.TextField()

    writing_type = models.CharField(
        max_length=20,
        choices=WRITING_TYPES,
        default='sher'
    )

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default='urdu'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.title