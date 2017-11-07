from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from core.models import Queue
from core.forms import QueueForm
from django.core.urlresolvers import reverse_lazy

class QueueCreate(CreateView):
	model = Queue
	form_class = QueueForm
	success_url = reverse_lazy('list_queue')


class QueueListView(ListView):
	model = Queue