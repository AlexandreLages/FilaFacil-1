from django import forms
from core.models import *

class CompanyForm(forms.ModelForm):

	class Meta:
		model = Company
		fields = ('name', 'cnpj', 'description')


class PointOfServiceForm(forms.ModelForm):

	class Meta:
		model = PointOfService
		fields = ('name', 'description', 'address', 'company')