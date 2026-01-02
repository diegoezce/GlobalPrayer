from django.urls import path
from . import views

urlpatterns = [
    path('<int:group_id>/prayer-requests/', views.prayer_requests_list, name='prayer_requests_list'),
    path('<int:group_id>/add-prayer-request/', views.add_prayer_request, name='add_prayer_request'),
    path('family-groups/', views.family_groups_list, name='family_groups_list'),
    path('add-family-group/', views.add_family_group, name='add_family_group'),
]