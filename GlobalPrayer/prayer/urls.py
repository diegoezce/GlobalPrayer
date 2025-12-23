from django.urls import path
from .views import world_map, pray_for_country

urlpatterns = [
    path("", world_map, name="world_map"),
    path("pray/<str:iso3>/", pray_for_country, name="pray_for_country"),
]