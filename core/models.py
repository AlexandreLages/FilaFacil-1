from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(models.Model):
	name = models.TextField(max_length=100, blank=False, null=False)
	cpf = models.TextField(max_length=11, blank=False, null=False)
	descrition = models.TextField(max_length=100, blank=True, null=True)
	firebase_token = models.TextField(max_length=200, blank=True, null=True)