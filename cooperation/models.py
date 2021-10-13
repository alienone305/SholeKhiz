from django.db import models
from django.utils import timezone

class JobOpportunityModel(models.Model):
    job_title = models.CharField(max_length = 264, blank = False, null = False)
    required_skills = models.TextField(null = False, blank = False)
    descriprion = models.TextField(null = False, blank = False)


class ApplicationModel(models.Model):
    job = models.ForeignKey(JobOpportunityModel, on_delete = models.CASCADE,
                                null = False, blank = False, related_name = 'applications')
    name = models.CharField(max_length = 264, blank = False, null = False)
    last_name = models.CharField(max_length = 264, blank = False, null = False)
    email = models.EmailField(blank = False, null = False)
    id_number = models.IntegerField(blank = False, null = False)
    age = models.IntegerField(blank = False, null = False)
    is_man = models.BooleanField(default = True)
    is_single = models.BooleanField(default = True)
    phone_number = models.IntegerField(blank = False, null = False)
    cellphone_number = models.IntegerField(blank = False, null = False)
    address = models.TextField(null = False, blank = False)

    college_evidence = models.CharField(max_length = 264, blank = True, null = True)
    field_of_study = models.CharField(max_length = 264, blank = True, null = True)
    college_score = models.IntegerField(blank = True, null = True)
    name_of_college = models.CharField(max_length = 264, blank = True, null = True)
    english_mastery = models.CharField(max_length = 264, blank = True, null = True)
    computer_mastery = models.CharField(max_length = 264, blank = True, null = True)
    job_attendance = models.CharField(max_length = 264, blank = True, null = True)
    descriprion = models.TextField(null = True, blank = True)
    resome = models.FileField(upload_to='resome/',null = True, blank = True, default = r'cataloges/default/default.jpeg')



class DelegationRequestModel(models.Model):
    name = models.CharField(max_length = 264, blank = False, null = False)
    last_name = models.CharField(max_length = 264, blank = False, null = False)
    email = models.EmailField(blank = False, null = False)
    age = models.IntegerField(blank = False, null = False)
    province = models.CharField(max_length = 264, blank = False, null = False)
    city = models.CharField(max_length = 264, blank = False, null = False)
    phone_number = models.IntegerField(blank = False, null = False)
    cellphone_number = models.IntegerField(blank = False, null = False)
    address = models.TextField(null = False, blank = False)
    area = models.IntegerField(blank = False, null = False)
    for_towerdryer = models.BooleanField(default = False)
    for_package = models.BooleanField(default = False)
    for_radiator = models.BooleanField(default = False)
    for_waterheater = models.BooleanField(default = False)
    has_reservoir = models.BooleanField(default = False)

    fax_number = models.IntegerField(blank = True, null = True)
    sell_prediction_towerdryer = models.IntegerField(blank = True, null = True)
    sell_prediction_package = models.IntegerField(blank = True, null = True)
    sell_prediction_radiator = models.IntegerField(blank = True, null = True)
    sell_prediction_waterheater = models.IntegerField(blank = True, null = True)
    attendance = models.CharField(max_length = 264, blank = True, null = True)
    description = models.TextField(null = True, blank = True)
    ownership_type = models.CharField(max_length = 264, blank = True, null = True)


class RepairManRequestModel(models.Model):
    name = models.CharField(max_length = 264, blank = False, null = False)
    last_name = models.CharField(max_length = 264, blank = False, null = False)
    age = models.IntegerField(blank = False, null = False)
    province = models.CharField(max_length = 264, blank = False, null = False)
    city = models.CharField(max_length = 264, blank = False, null = False)
    is_single = models.BooleanField(default = True)
    phone_number = models.IntegerField(blank = False, null = False)
    cellphone_number = models.IntegerField(blank = False, null = False)
    address = models.TextField(null = False, blank = False)
    for_towerdryer = models.BooleanField(default = False)
    for_package = models.BooleanField(default = False)
    for_radiator = models.BooleanField(default = False)
    for_waterheater = models.BooleanField(default = False)

    college_evidence = models.CharField(max_length = 264, blank = True, null = True)
    field_of_study = models.CharField(max_length = 264, blank = True, null = True)
    college_score = models.IntegerField(blank = True, null = True)
    name_of_college = models.CharField(max_length = 264, blank = True, null = True)
    has_office = models.BooleanField(default = False)
    can_travel = models.BooleanField(default = False)
    attendance = models.TextField(null = True, blank = True)
    experience = models.TextField(null = True, blank = True)
    certificates = models.TextField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)
