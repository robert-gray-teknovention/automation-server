from django.core.management.base import BaseCommand
from controller.models import Function
from django.conf import settings
if settings.SYSTEM == 'pi':
    import controller.functions as functions
else:
    import controller.pifunctions as functions
import inspect
import json
print(settings.SYSTEM)


class Command(BaseCommand):
    help = 'This command reads functions.py and registers and saves into database.'

    def handle(self, *args, **kwargs):
        print("We are reading and registering functions.")
        # functions = Import_module('controller.functions')
        for f in inspect.getmembers(functions, inspect.isfunction):
            func, created = Function.objects.get_or_create(name=f[0])
            argsstring = json.dumps(inspect.getfullargspec(f[1]).args)
            func.args = argsstring
            func.save()
            print(func.name, ' ', func.args)
