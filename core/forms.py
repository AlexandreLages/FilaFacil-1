from django import forms
from core.models import *

class CompanyForm(forms.ModelForm):

	class Meta:
		model = Company
		fields = ('name',)