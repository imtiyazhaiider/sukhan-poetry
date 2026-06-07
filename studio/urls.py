from django.urls import path

from .views import (
    radeef_checker,
    qaafiya_checker,
    writer_tools,
    writing_dashboard,
    studio_editor,
    my_drafts,
    edit_draft,
    delete_draft,
    publish_draft
)

urlpatterns = [

    path(
        'studio/',
        studio_editor,
        name='studio_editor'
    ),

    path(
        'studio/radeef/',
        radeef_checker,
        name='radeef_checker'
    ),

    path(
    'studio/qaafiya/',
    qaafiya_checker,
    name='qaafiya_checker'
    ),

    path(
    'studio/tools/',
    writer_tools,
    name='writer_tools'
    ),

    path(
    'studio/dashboard/',
    writing_dashboard,
    name='writing_dashboard'
    ),

    path(
        'studio/drafts/',
        my_drafts,
        name='my_drafts'
    ),

    path(
        'studio/drafts/<int:draft_id>/edit/',
        edit_draft,
        name='edit_draft'
    ),

    path(
        'studio/drafts/<int:draft_id>/delete/',
        delete_draft,
        name='delete_draft'
    ),

    path(
        'studio/drafts/<int:draft_id>/publish/',
        publish_draft,
        name='publish_draft'
    ),

]