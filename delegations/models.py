from django.db import models

class DelegationModel(models.Model):
    province = models.CharField(max_length = 264, blank = False, null = False)
    address = models.TextField(null = True, blank = True)
    phone_number = models.CharField(max_length = 264, blank = True, null =True)
