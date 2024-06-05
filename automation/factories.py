from .mqtt import MqttConnection
from django.conf import settings
from datetime import datetime
import threading
from automation.models import MqttBroker
import json
import time

if settings.SYSTEM == 'pi':
    import command.pifunctions as functions
else:
    import command.functions as functions


class Commander():
    def __init__(self, client):
        self.client = client

    def finished(self, cmd):
        cmd.executed = True
        cmd.end = settings.TZ.localize(datetime.now())
        cmd.save()

    def remote_finished(self, cmd, callback):
        if callback:
            timeout = time.perf_counter() + cmd.function.response_timeout
            while time.perf_counter() < timeout:
                cmd.refresh_from_db()
                if cmd.executed:
                    callback(cmd)
                    print("Command Finished! ", cmd.return_message)
                    break
                else:
                    time.sleep(.5)
                    print("not complete")

    def run_threaded(self, job, args):
        thread = threading.Thread(target=job, args=args, kwargs={})
        thread.start()
        # print(thread.result)

    def run_remote(self, cmd, callback=None):
        msg = {
            'type': 'cmd',
            'target': str(cmd.function.device.device_id),
            'command': {
                "id": cmd.id,
                "function": cmd.function.name,
                "async": cmd.function.asyncro,
                "args": cmd.args,
                "server": settings.SYSTEM
            }
        }
        self.client.publish(cmd.function.device.topic.get_name(), json.dumps(msg))
        if callback:
            self.run_threaded(self.remote_finished, [cmd, callback])
        # response = client.message_queue.get()
        # print("Response ", str(response))

    def run(self, cmd, callback=None, **kwargs):
        if not cmd.id:
            args = []
            args.extend(cmd.args)
            cmd.start = settings.TZ.localize(datetime.now())
            cmd.save()
            if not cmd.function.remote:
                def serialize_datetime(obj):
                    if isinstance(obj, datetime):
                        return obj.isoformat()
                    raise TypeError("Type not serializable")

                rm = {
                    'cmd_id': cmd.id,
                    'server': settings.SYSTEM,
                    'type': 'local',
                    'timestamp': serialize_datetime(settings.TZ.localize(datetime.now()))
                }

                func = getattr(functions, cmd.function.name)

                if cmd.function.asyncro:
                    args.append(lambda: self.finished(cmd))
                    rm['ret_value'] = "ASYNC"
                    self.run_threaded(func, args)

                else:
                    rm['ret_value'] = func(*args)
                    cmd.return_message = json.dumps(rm)
                    self.finished(cmd)
            else:
                self.run_remote(cmd, callback)
        else:
            print("Command not sent, already executed")


server = MqttBroker.objects.first()
client = MqttConnection(server)
client.connect()
commander = Commander(client)
