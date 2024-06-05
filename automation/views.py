from django.views.generic.list import ListView
from command.models import Function


class FunctionListView(ListView):
    queryset = Function.objects.filter(active=True).order_by('device', 'read_write')
