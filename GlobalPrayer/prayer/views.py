from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Country

def world_map(request):
    countries = Country.objects.all()
    return render(request, "prayer/map.html", {
        "countries": countries
    })

def home(request):
    return render(request, "prayer/home.html")

@csrf_exempt
@require_POST
def pray_for_country(request, iso3):
    iso3 = iso3.upper()

    country_name = iso3

    if request.body:
        try:
            import json
            body = json.loads(request.body.decode("utf-8"))
            country_name = body.get("name", iso3)
        except Exception:
            pass

    country, created = Country.objects.get_or_create(
        iso_code=iso3,
        defaults={
            "name": country_name,
            "prayer_count": 0,
        }
    )

    country.prayer_count += 1
    country.save()

    return JsonResponse({
        "ok": True,
        "iso": iso3,
        "name": country.name,
        "created": created,
        "prayer_count": country.prayer_count
    })