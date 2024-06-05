import time
import threading
import asyncio
import inspect
import json
from . import functions
from django.core.exceptions import ObjectDoesNotExist
import traceback
from django.conf import settings
# Here is a test for .gitignore
default_description = {
    "response_timeout": 5,
    "type": "sync",
    "read_write": "read"
}


def insert_function_list(device):
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
                print("we are iterating")
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


def read_functions():
    '''{"read_write": "read", "response_timeout": 5, "type": "sync"}'''
    funcs = []
    for f in inspect.getmembers(functions, inspect.isfunction):
        if f[1].__doc__:
            func = {
                'func_name': f[0],
            }
            func.update(default_description)
            print(str(f[1].__doc__))
            func.update(json.loads(str(f[1].__doc__)))

            args = inspect.getfullargspec(f[1]).args
            if args and (args[-1] in ['cb', 'callback']):
                args.pop()
            func['args'] = args
            funcs.append(func)
    return {'device': settings.SYSTEM, 'items': funcs}


def test_function(var):
    '''{}'''
    print(var)
    return var


def test_function_sync(var, duration=5):
    time.sleep(int(duration))
    print(var)
    return var


def test_function_threaded(var, duration, cb):
    '''{"type": "async"}'''
    def thread_func(var, duration, cb):
        time.sleep(duration)
        cb("Threaded OK")
    thread = threading.Thread(target=thread_func, args=(var, duration, cb))
    thread.start()


async def test_function_async(var, duration, cb):
    print("we are starting async function")
    count = 0
    while count in range(duration):
        await asyncio.sleep(1)
        print('waiting')
        count += 1
    print("We are going to send a return message!!")
    cb(var)
