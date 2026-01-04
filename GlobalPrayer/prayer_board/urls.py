from django.urls import path
from . import views

urlpatterns = [
    path('', views.prayer_board_landing, name='prayer_board_landing'),
    path('<int:group_id>/prayer-requests/', views.prayer_requests_list, name='prayer_requests_list'),
    path('<int:group_id>/add-prayer-request/', views.add_prayer_request, name='add_prayer_request'),
    path('prayer-request/<int:request_id>/prayed/', views.mark_as_prayed, name='mark_as_prayed'),
    path('family-groups/', views.family_groups_list, name='family_groups_list'),
    path('add-family-group/', views.add_family_group, name='add_family_group'),
    path("prayer-request/<int:request_id>/answered/",views.mark_as_answered,name="mark_as_answered"),
    path(
    "group/<int:group_id>/enter/",
    views.enter_group_code,
    name="enter_group_code",
    ),
    path(
    'group/<int:group_id>/created/',
    views.family_group_created,
    name='family_group_created'
    ),
]