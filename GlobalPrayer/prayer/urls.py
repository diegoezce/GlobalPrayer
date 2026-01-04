from django.urls import path
from .views import home, world_map, pray_for_country
urlpatterns = [
    path("", home, name="home"),
    path("map/", world_map, name="map"),
    path("pray/<str:iso3>/", pray_for_country, name="pray_for_country"),
]