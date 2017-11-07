from django import forms
from core.models import *

class CompanyForm(forms.ModelForm):
	name = forms.CharField(max_length=100, required=True)
	description = forms.CharField(max_length=200, required=False)
	cnpj = forms.CharField(max_length=100, required=True)

	class Meta:
		model = Company
		fields = ('name', 'cnpj', 'description')


class PointOfServiceForm(forms.ModelForm):
	name = forms.CharField(max_length=100, required=True)
	description = forms.CharField(max_length=200, required=False)
	address = forms.CharField(max_length=100, required=True)
	
	class Meta:
		model = PointOfService
		fields = ('name', 'description', 'address', 'company')


class QueueForm(forms.ModelForm):
	name = forms.CharField(max_length=100, required=True)
	description = forms.CharField(max_length=200, required=False)
	
	class Meta:
		model = Queue
		fields = ('name', 'description', 'start_time', 'end_time', 'point_of_service')