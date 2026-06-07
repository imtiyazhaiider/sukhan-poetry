from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Poet(models.Model):

    name = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    biography = models.TextField()

    birth_year = models.IntegerField(blank=True, null=True)

    death_year = models.IntegerField(blank=True, null=True)

    image = models.ImageField(
        upload_to='poets/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Writing(models.Model):

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

    title = models.CharField(max_length=255)

    slug = models.SlugField(blank=True)

    poet = models.ForeignKey(
        Poet,
        on_delete=models.CASCADE,
        related_name='writings'
    )

    content = models.TextField()

    writing_type = models.CharField(
        max_length=20,
        choices=WRITING_TYPES
    )

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES
    )

    categories = models.ManyToManyField(Category)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Submission(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

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

    poet_name = models.CharField(max_length=255)

    poet_biography = models.TextField(
        blank=True
    )

    title = models.CharField(max_length=255)

    content = models.TextField()

    writing_type = models.CharField(
        max_length=20,
        choices=WRITING_TYPES
    )

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES
    )

    submitted_by = models.CharField(
        max_length=255,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title} ({self.status})"


class Favorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites'
    )

    writing = models.ForeignKey(
        Writing,
        on_delete=models.CASCADE,
        related_name='favorited_by'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = (
            'user',
            'writing'
        )

    def __str__(self):

        return f"{self.user.username} ❤️ {self.writing.title}"