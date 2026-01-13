from django.db import models

class FamilyGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_private = models.BooleanField(default=False)
    access_code = models.CharField(max_length=4, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PrayerRequest(models.Model):
    family_group = models.ForeignKey(FamilyGroup, on_delete=models.CASCADE, related_name='prayer_requests')
    title = models.CharField(max_length=255)
    description = models.TextField()
    prayed_count = models.PositiveIntegerField(default=0)
    last_prayed_at = models.DateTimeField(null=True, blank=True)
    is_answered = models.BooleanField(default=False)
    answered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class PrayerComment(models.Model):
    prayer_request = models.ForeignKey(
        PrayerRequest,
        related_name="comments",
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)