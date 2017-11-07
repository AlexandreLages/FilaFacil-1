from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from core.models import PointOfService
from core.forms import PointOfServiceForm
from django.core.urlresolvers import reverse_lazy

class PointOfServiceCreate(CreateView):
	model = PointOfService
	form_class = PointOfServiceForm
	success_url = reverse_lazy('list_point')


class PointOfServiceListView(ListView):
	model = PointOfService