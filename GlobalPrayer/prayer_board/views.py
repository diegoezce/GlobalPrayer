from django.shortcuts import render, get_object_or_404, redirect
from .models import FamilyGroup, PrayerRequest

def prayer_requests_list(request, group_id):
    family_group = get_object_or_404(FamilyGroup, id=group_id)
    prayer_requests = family_group.prayer_requests.all()
    return render(request, 'prayer_board/prayer_requests_list.html', {
        'family_group': family_group,
        'prayer_requests': prayer_requests,
    })

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
        if name:
            FamilyGroup.objects.create(name=name, description=description)
            return redirect('family_groups_list')  # Redirect to the list of family groups
    return render(request, 'prayer_board/add_family_group.html')

def family_groups_list(request):
    family_groups = FamilyGroup.objects.all()
    return render(request, 'prayer_board/family_groups_list.html', {
        'family_groups': family_groups,
    })


def prayer_board_landing(request):
    return render(request, "prayer_board/landing.html")