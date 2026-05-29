from django.urls import path
from . import views

urlpatterns = [

    path(
        'poets/<slug:slug>/',
        views.poet_detail,
        name='poet_detail'
    ),

    path(
        'writings/<slug:slug>/',
        views.writing_detail,
        name='writing_detail'
    ),

    path(
        'search/',
        views.search,
        name='search'
    ),

    path(
        'random/',
        views.random_poetry,
        name='random_poetry'
    ),

    path(
        'submit/',
        views.submit_writing,
        name='submit_writing'
    ),

]