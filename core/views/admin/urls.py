from django.conf.urls import url, include
from core.views.admin.company import CompanyCreate, CompanyListView

urlpatterns = [
	url(r'^empresas/criar/$', CompanyCreate.as_view(), name='add_company'),
	url(r'^empresas/$', CompanyListView.as_view(), name='list_company'),
]