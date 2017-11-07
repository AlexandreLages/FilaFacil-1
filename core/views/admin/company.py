from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from core.models import Company
from core.forms import CompanyForm
from django.core.urlresolvers import reverse_lazy

class CompanyCreate(CreateView):
	model = Company
	form_class = CompanyForm
	success_url = reverse_lazy('list_company')


class CompanyListView(ListView):
	model = Company