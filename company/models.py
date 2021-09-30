from django.db import models
from django.utils import timezone

class ContactUsModel(models.Model):
    name = models.CharField(max_length = 264, blank = False, null = False)
    email = models.EmailField(blank = False, null = False)
    phone_number = models.CharField(max_length = 264, blank = True, null =True)
    request = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(default=timezone.now())
