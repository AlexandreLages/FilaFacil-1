from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(models.Model):
	name = models.TextField(max_length=100, blank=False, null=False)
	cpf = models.TextField(max_length=11, blank=False, null=False)
	descrition = models.TextField(max_length=100, blank=True, null=True)
	firebase_token = models.TextField(max_length=200, blank=True, null=True)

 	
class Company(models.Model):
	name = models.TextField(max_length=100, blank=False, null=False)
	cnpj = models.TextField(max_length=100, blank=False, null=False, unique=True)
	description = models.TextField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.name


class PointOfService(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	address = models.TextField(max_length=200, blank=False, null=False)
	description = models.TextField(max_length=200, blank=True, null=True)
	name = models.TextField(max_length=100, blank=False, null=False)


class Queue(models.Model):
	point_of_service = models.ForeignKey(PointOfService, on_delete=models.CASCADE)
	name = models.TextField(max_length=100, blank=False, null=False)
	description = models.TextField(max_length=200, blank=True, null=True)
	start_time = models.TimeField(blank=False, null=False)
	end_time = models.TimeField(blank=False, null=False)