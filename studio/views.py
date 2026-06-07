from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .forms import DraftForm
from .models import Draft

from poetry.models import Submission


@login_required
def studio_editor(request):

    if request.method == 'POST':

        form = DraftForm(request.POST)

        if form.is_valid():

            draft = form.save(commit=False)

            draft.user = request.user

            draft.save()

            return redirect('my_drafts')

    else:

        form = DraftForm()

    return render(
        request,
        'studio/editor.html',
        {
            'form': form
        }
    )


@login_required
def my_drafts(request):

    drafts = Draft.objects.filter(
        user=request.user
    ).order_by('-updated_at')

    return render(
        request,
        'studio/my_drafts.html',
        {
            'drafts': drafts
        }
    )


@login_required
def edit_draft(request, draft_id):

    draft = get_object_or_404(
        Draft,
        id=draft_id,
        user=request.user
    )

    if request.method == 'POST':

        form = DraftForm(
            request.POST,
            instance=draft
        )

        if form.is_valid():

            form.save()

            return redirect('my_drafts')

    else:

        form = DraftForm(
            instance=draft
        )

    return render(
        request,
        'studio/editor.html',
        {
            'form': form,
            'draft': draft
        }
    )


@login_required
def delete_draft(request, draft_id):

    draft = get_object_or_404(
        Draft,
        id=draft_id,
        user=request.user
    )

    draft.delete()

    return redirect('my_drafts')


@login_required
def publish_draft(request, draft_id):

    draft = get_object_or_404(
        Draft,
        id=draft_id,
        user=request.user
    )

    Submission.objects.create(
        poet_name=request.user.username,
        poet_biography='',
        title=draft.title,
        content=draft.content,
        writing_type=draft.writing_type,
        language=draft.language,
        submitted_by=request.user.username,
        status='pending'
    )

    draft.delete()

    return redirect('my_drafts')

@login_required
def radeef_checker(request):

    result = None

    if request.method == 'POST':

        poetry = request.POST.get(
            'poetry',
            ''
        )

        lines = [
            line.strip()
            for line in poetry.split('\n')
            if line.strip()
        ]

        last_words = []

        for line in lines:

            words = line.split()

            if words:

                last_words.append(
                    words[-1]
                )

        if last_words:

            from collections import Counter

            counter = Counter(
                last_words
            )

            most_common = counter.most_common(1)

            if most_common:

                result = most_common[0][0]

    return render(
        request,
        'studio/radeef_checker.html',
        {
            'result': result
        }
    )

@login_required
def qaafiya_checker(request):

    radeef = None
    qaafiya_words = []

    if request.method == 'POST':

        poetry = request.POST.get(
            'poetry',
            ''
        )

        lines = [
            line.strip()
            for line in poetry.split('\n')
            if line.strip()
        ]

        split_lines = []

        for line in lines:

            words = line.split()

            if len(words) >= 2:

                split_lines.append(words)

        if split_lines:

            last_words = [
                words[-1]
                for words in split_lines
            ]

            from collections import Counter

            counter = Counter(last_words)

            common = counter.most_common(1)

            if common:

                radeef = common[0][0]

                for words in split_lines:

                    if words[-1] == radeef:

                        qaafiya_words.append(
                            words[-2]
                        )

    return render(
        request,
        'studio/qaafiya_checker.html',
        {
            'radeef': radeef,
            'qaafiya_words': qaafiya_words
        }
    )

@login_required
def writer_tools(request):

    return render(
        request,
        'studio/tools.html'
    )

@login_required
def writing_dashboard(request):

    drafts_count = Draft.objects.filter(
        user=request.user
    ).count()

    pending_count = Submission.objects.filter(
        submitted_by=request.user.username,
        status='pending'
    ).count()

    approved_count = Submission.objects.filter(
        submitted_by=request.user.username,
        status='approved'
    ).count()

    rejected_count = Submission.objects.filter(
        submitted_by=request.user.username,
        status='rejected'
    ).count()

    recent_drafts = Draft.objects.filter(
        user=request.user
    ).order_by('-updated_at')[:5]

    recent_submissions = Submission.objects.filter(
        submitted_by=request.user.username
    ).order_by('-created_at')[:5]

    return render(
        request,
        'studio/dashboard.html',
        {
            'drafts_count': drafts_count,
            'pending_count': pending_count,
            'approved_count': approved_count,
            'rejected_count': rejected_count,
            'recent_drafts': recent_drafts,
            'recent_submissions': recent_submissions,
        }
    )