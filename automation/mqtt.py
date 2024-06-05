import paho.mqtt.client as mqtt
import ssl
from queue import Queue
import json
from command.models import Command
from django.conf import settings
from datetime import datetime
import command.functions as functions
import asyncio


class MqttConnection():
    def __init__(self, server):
        self.server = server
        self.message_queue = Queue()

    def connect(self):
        self.client = mqtt.Client()  # This queue doesn't do anything yet
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(self.server.username, self.server.password)
        self.client.tls_set(cert_reqs=ssl.CERT_NONE)
        self.client.connect(
            host=self.server.host,
            port=self.server.port,
            keepalive=60
        )
        print(str(self.server))
        print("We just tried connecting!!")
        self.client.loop_start()

    def is_connected(self):
        return self.client.is_connected()

    def on_connect(self, mqtt_client, userdata, flags, rc):
        if rc == 0:
            print('Connected successfully')
            topics = self.server.topic_set.all()
            for t in topics:
                mqtt_client.subscribe(t.get_name())
        else:
            print('Bad connection. Code:', rc)

    def on_message(self, mqtt_client, userdata, msg):
        # print(msg.payload.decode('utf-8'))
        def serialize_datetime(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError("Type not serializable")

        ret_msg = json.loads(msg.payload.decode("utf-8"))
        if "type" in ret_msg:
            if ret_msg['type'] == 'response' and ret_msg['server'] == settings.SYSTEM:
                try:
                    cmd = Command.objects.get(id=ret_msg['cmd_id'])
                    if not cmd.executed:
                        cmd.end = settings.TZ.localize(datetime.now())
                        # ret_msg['timestamp'] = json.dumps(cmd.end, default=serialize_datetime)
                        ret_msg['timestamp'] = serialize_datetime(cmd.end)
                        cmd.return_message = json.dumps(ret_msg)
                        cmd.executed = True
                        cmd.save()
                        print("We just updated the command ", cmd.id, ' ', cmd.function.name)
                    else:
                        print("We did not save this command.  It was already executed.")
                except Command.DoesNotExist:
                    print("This command was not found in the database")
                except Exception as e:
                    print("General exception ", e)

            elif ret_msg['type'] == 'cmd' and ret_msg['target'] == settings.SYSTEM:
                # func.getattr(functions, ret_msg['command']['function'])
                # func.getattr()
                print("message topic: ", msg.topic)
                self.process_cmd(ret_msg['command'], msg.topic)
            elif ret_msg['type'] == 'ping':
                pass
            else:
                print("This command was not sent by this server, or it's not a response")

            # self.message_queue.put(msg.payload)

    def process_cmd(self, cmd, topic):
        server = 'None'
        if 'server' in cmd:
            server = cmd['server']
        try:
            func = getattr(functions, cmd['function'])
            if cmd['async'] is True:
                def pub_msg(ret_value):
                    ret_msg = {
                        'cmd_id': cmd['id'],
                        'server': server,
                        'ret_value': ret_value,
                        'type': 'response',
                        }
                    self.publish(topic, bytes(json.dumps(ret_msg), 'utf-8'))

                cmd['args'].append(pub_msg)
                print("func ", str(pub_msg))
                # loop = asyncio.new_event_loop()
                # loop.run_until_complete(self.run_command(func(*cmd['args'])))
                print(str(cmd['args']))
                func(*cmd['args'])
            else:
                ret_msg = {
                    'cmd_id': cmd['id'],
                    'server': server,
                    'ret_value': func(*cmd['args']),
                    'type': 'response',
                    }
                self.publish(topic, bytes(json.dumps(ret_msg), 'utf-8'))
        except Exception as e:
            except_msg = {
                'cmd_id': cmd['id'],
                'server': server,
                'ret_value': 'Error:' + str(e),
                'type': 'response',
                }
            self.publish(topic, bytes(json.dumps(except_msg), 'utf-8'))

    def publish(self, topic, msg):
        self.client.publish(topic, msg)
