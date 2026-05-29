from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)

from django.db.models import Q

from .models import (
    Poet,
    Writing
)

from .forms import SubmissionForm

import random


def poet_detail(request, slug):

    poet = get_object_or_404(
        Poet,
        slug=slug
    )

    writings = poet.writings.all()

    context = {
        'poet': poet,
        'writings': writings,
    }

    return render(
        request,
        'poetry/poet_detail.html',
        context
    )


def writing_detail(request, slug):

    writing = get_object_or_404(
        Writing,
        slug=slug
    )

    context = {
        'writing': writing,
    }

    return render(
        request,
        'poetry/writing_detail.html',
        context
    )


def search(request):

    query = request.GET.get('q', '')

    poets = Poet.objects.none()
    writings = Writing.objects.none()

    if query:

        poets = Poet.objects.filter(
            name__icontains=query
        )

        writings = Writing.objects.filter(
            title__icontains=query
        )

    context = {
        'query': query,
        'poets': poets,
        'writings': writings,
    }

    return render(
        request,
        'poetry/search.html',
        context
    )


def random_poetry(request):

    writings = Writing.objects.all()

    if not writings.exists():

        return redirect('/')

    writing = random.choice(writings)

    return redirect(
        'writing_detail',
        slug=writing.slug
    )


def submit_writing(request):

    if request.method == 'POST':

        form = SubmissionForm(request.POST)

        if form.is_valid():

            form.save()

            return render(
                request,
                'poetry/submission_success.html'
            )

    else:

        form = SubmissionForm()

    context = {
        'form': form
    }

    return render(
        request,
        'poetry/submit_writing.html',
        context
    )