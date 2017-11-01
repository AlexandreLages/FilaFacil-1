from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from core.models import PointOfService
from core.forms import PointOfServiceForm

class PointOfServiceCreate(CreateView):
	model = PointOfService
	form_class = PointOfServiceForm
	success_url = ('list_company')


class PointOfServiceListView(ListView):
	model = PointOfService