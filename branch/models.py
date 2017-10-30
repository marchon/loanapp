import datetime

from django.db import models
from django.utils import timezone

class BasicInfo(models.Model):
	last_name = models.CharField()
	first_name = models.CharField()
	middle_name = models.CharField()
	gender= models.CharField(max_length=1)
	birthdate = models.DateField()
	civil_status = models.CharField()
	address = models.CharField()
	telephone = models.CharField()
	mobile = models.CharField()
	sss = models.CharField()
	gsis = models.CharField()
	active_status = models.BooleanField()