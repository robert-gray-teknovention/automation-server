from django.core.exceptions import ObjectDoesNotExist
import traceback
import inspect
from django.conf import settings


class UtilityFunctionsMixin():
    '''This class contains utility functions that are run locally and are global for all the different installs'''

    def insert_function_list(self, device):
        from automation.factories import commander
        from .models import Function, Command, Device
        rw_choices = Function.ReadWriteChoices

        def remote_callback(cmd):
            def get_asyncro(type):
                return True if type == 'async' else False
            import json
            try:
                ret_message = json.loads(cmd.return_message)
                device = Device.objects.get(device_id=ret_message['ret_value']['device'])
                old_list = Function.objects.filter(device=device)
                old_list.update(active=False)
                for f in old_list:
                    f.save()

                for item in ret_message['ret_value']['items']:
                    try:
                        rw = getattr(rw_choices, item['read_write'].upper())

                    except Exception as e:
                        rw = rw_choices.NONE
                        print(e)
                        print("There is an error with assigning read_write, check read_write is set as comment")

                    try:
                        func = Function.objects.get(name=item['func_name'], device=device)
                        func.args = item['args']
                        func.asyncro = get_asyncro(item['type'])
                        func.remote = True
                        func.active = True
                        func.read_write = rw
                    except ObjectDoesNotExist:
                        # Put new function in database
                        func = Function()
                        func.name = item['func_name']
                        func.args = item['args']
                        func.active = True
                        func.device = device
                        func.asyncro = get_asyncro(item['type'])
                        func.remote = True
                        func.read_write = rw
                    func.save()
                    print("We just saved our Function!!")

            except Exception as e:
                print("We have an error ***************", e)
                print(traceback.format_exc())

        rf = Function.objects.get(name='read_functions', device=device)
        cmd = Command()
        cmd.function = rf
        cmd.args = []
        commander.run(cmd, remote_callback)

    def add_default_device_types():
        from .models import DeviceType
        types = settings.DEVICE_TYPES
        for t in types:
            device, created = DeviceType.objects.get_or_create(name=t)
            print(device.name, " ", created)

    def read_functions(self):
        '''{"read_write": "read", "response_timeout": 5, "type": "sync"}'''
        default_description = {
            "response_timeout": 5,
            "type": "sync",
            "read_write": "read"
        }
        import json
        funcs = []
        for f in inspect.getmembers(self, inspect.ismethod):
            if f[1].__doc__:
                func = {
                    'func_name': f[0],
                }
                func.update(default_description)
                func.update(json.loads(str(f[1].__doc__)))
                args = inspect.getfullargspec(f[1]).args
                args.pop(0)  # Remove the cls argument from class inspection
                if args and (args[-1] in ['cb', 'callback']):
                    args.pop()
                func['args'] = args
                funcs.append(func)
        return {'device': settings.SYSTEM, 'items': funcs}
