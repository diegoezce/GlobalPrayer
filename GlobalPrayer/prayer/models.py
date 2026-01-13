from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    iso_code = models.CharField(
        max_length=3,
        unique=True,
        help_text="Código ISO-3166 alpha-3 (ej: ARG, USA, BRA)"
    )
    prayer_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class PrayerCommitment(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

