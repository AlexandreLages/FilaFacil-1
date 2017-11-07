from django.conf.urls import url, include
from core.views.admin.company import CompanyCreate, CompanyListView
from core.views.admin.point_of_service import PointOfServiceCreate, PointOfServiceListView
from core.views.admin.queue import QueueCreate, QueueListView

urlpatterns = [
	url(r'^empresas/criar/$', CompanyCreate.as_view(), name='add_company'),
	url(r'^empresas/$', CompanyListView.as_view(), name='list_company'),

	url(r'^pontos/criar/$', PointOfServiceCreate.as_view(), name='add_point'),
	url(r'^pontos/$', PointOfServiceListView.as_view(), name='list_point'),

	url(r'^filas/criar/$', QueueCreate.as_view(), name='add_queue'),
	url(r'^filas/$', QueueListView.as_view(), name='list_queue')
]