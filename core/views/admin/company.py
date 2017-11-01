from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from core.models import Company
from core.forms import CompanyForm

class CompanyCreate(CreateView):
	model = Company
	form_class = CompanyForm
	success_url = ('list_company')


class CompanyListView(ListView):
	model = Company