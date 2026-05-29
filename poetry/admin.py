from django.contrib import admin
from django.utils.text import slugify

from .models import (
    Poet,
    Writing,
    Category,
    Submission
)


@admin.register(Poet)
class PoetAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'birth_year',
        'death_year'
    )

    search_fields = (
        'name',
    )


@admin.register(Writing)
class WritingAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'poet',
        'writing_type',
        'language',
        'created_at'
    )

    search_fields = (
        'title',
        'content'
    )

    list_filter = (
        'writing_type',
        'language'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'poet_name',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'language',
        'writing_type'
    )

    search_fields = (
        'title',
        'poet_name',
        'content'
    )

    def save_model(
        self,
        request,
        obj,
        form,
        change
    ):

        newly_approved = False

        if obj.pk:

            old_obj = Submission.objects.get(
                pk=obj.pk
            )

            if (
                old_obj.status != 'approved'
                and obj.status == 'approved'
            ):
                newly_approved = True

        super().save_model(
            request,
            obj,
            form,
            change
        )

        if newly_approved:

            poet_slug = slugify(
                obj.poet_name
            )

            poet, created = Poet.objects.get_or_create(
                slug=poet_slug,
                defaults={
                    'name': obj.poet_name,
                    'biography': obj.poet_biography
                }
            )

            writing_slug = slugify(
                obj.title
            )

            writing = Writing.objects.create(
                title=obj.title,
                slug=writing_slug,
                poet=poet,
                content=obj.content,
                writing_type=obj.writing_type,
                language=obj.language
            )