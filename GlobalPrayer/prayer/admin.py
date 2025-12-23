from django.contrib import admin
from .models import Country  # Asegúrate de que el modelo Country esté definido en models.py

admin.site.register(Country)  # Registra el modelo en el panel de administración
