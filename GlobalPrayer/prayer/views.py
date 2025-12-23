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

@csrf_exempt
@require_POST
def pray_for_country(request, iso3):
    try:
        country = Country.objects.get(iso_code=iso3.upper())
        country.prayer_count += 1
        country.save()
        return JsonResponse({"ok": True, "iso": iso3})
    except Country.DoesNotExist:
        return JsonResponse({"ok": False, "error": "Country not found"}, status=404)