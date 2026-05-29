from django.shortcuts import render

from poetry.models import Poet, Writing


def home(request):

    featured_poets = Poet.objects.all()[:4]

    trending_writings = Writing.objects.all().order_by('-created_at')[:4]

    context = {
        'featured_poets': featured_poets,
        'trending_writings': trending_writings,
    }

    return render(request, 'core/home.html', context)