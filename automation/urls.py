from django.urls import path
from django.views.generic.base import TemplateView
from automation.views import FunctionListView
urlpatterns = [
    path('dashboard/', TemplateView.as_view(template_name="automation/dashboard.html"), name="dashboard   "),
    path('dashboard/functions/', FunctionListView.as_view(template_name="automation/functions.html"), name="functions"),
]
