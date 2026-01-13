from django.shortcuts import render, get_object_or_404, redirect
from .models import FamilyGroup, PrayerRequest, PrayerRequest, PrayerComment
from django.utils import timezone
import random

# Helper view to handle private group access
def enter_group_code(request, group_id):
    family_group = get_object_or_404(FamilyGroup, id=group_id)

    # If group is public, redirect directly
    if not family_group.is_private:
        return redirect('prayer_requests_list', group_id=group_id)

    error = None

    if request.method == "POST":
        code = request.POST.get("access_code")

        if code and code == family_group.access_code:
            request.session[f"group_{family_group.id}_access"] = True
            return redirect('prayer_requests_list', group_id=group_id)
        else:
            error = "Invalid code"

    return render(request, "prayer_board/enter_group_code.html", {
        "family_group": family_group,
        "error": error,
    })

def prayer_requests_list(request, group_id):
    family_group = get_object_or_404(FamilyGroup, id=group_id)

    if family_group.is_private:
        has_access = request.session.get(f"group_{family_group.id}_access")
        if not has_access:
            return redirect('enter_group_code', group_id=group_id)

    prayer_requests = family_group.prayer_requests.all()
    return render(request, 'prayer_board/prayer_requests_list.html', {
        'family_group': family_group,
        'prayer_requests': prayer_requests,
    })


# New view to mark a prayer request as prayed
def mark_as_prayed(request, request_id):
    prayer_request = get_object_or_404(PrayerRequest, id=request_id)

    if request.method == "POST":
        prayer_request.prayed_count += 1
        prayer_request.last_prayed_at = timezone.now()
        prayer_request.save()

    return redirect('prayer_requests_list', group_id=prayer_request.family_group.id)

def mark_as_answered(request, request_id):
    prayer_request = get_object_or_404(PrayerRequest, id=request_id)

    if request.method == "POST":
        if prayer_request.is_answered:
            prayer_request.is_answered = False
            prayer_request.answered_at = None
        else:
            prayer_request.is_answered = True
            prayer_request.answered_at = timezone.now()

        prayer_request.save()

    return redirect(
        'prayer_requests_list',
        group_id=prayer_request.family_group.id
    )


def add_prayer_request(request, group_id):
    family_group = get_object_or_404(FamilyGroup, id=group_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            PrayerRequest.objects.create(
                family_group=family_group,
                title=title,
                description=description
            )
            return redirect('prayer_requests_list', group_id=group_id)
    return render(request, 'prayer_board/add_prayer_request.html', {
        'family_group': family_group,
    })

def add_family_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        is_private = request.POST.get('is_private') == 'true'

        if name:
            access_code = None
            if is_private:
                import random
                access_code = str(random.randint(1000, 9999))

            group = FamilyGroup.objects.create(
                name=name,
                description=description,
                is_private=is_private,
                access_code=access_code
            )

            return redirect('family_group_created', group_id=group.id)

    return render(request, 'prayer_board/add_family_group.html')


def family_group_created(request, group_id):
    family_group = get_object_or_404(FamilyGroup, id=group_id)
    return render(
        request,
        'prayer_board/family_group_created.html',
        {'family_group': family_group}
    )


def family_groups_list(request):
    family_groups = FamilyGroup.objects.all()
    return render(request, 'prayer_board/family_groups_list.html', {
        'family_groups': family_groups,
    })


def prayer_board_landing(request):
    return render(request, "prayer_board/landing.html")



def add_prayer_comment(request, request_id):
    prayer_request = get_object_or_404(PrayerRequest, id=request_id)

    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        if text:
            PrayerComment.objects.create(
                prayer_request=prayer_request,
                text=text
            )

    return redirect("prayer_requests_list", prayer_request.family_group.id)