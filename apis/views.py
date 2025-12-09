from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import JsonResponse
from automation.factories import commander
import traceback
from .serializers import (
    UserSerializer,
    RealDataItemSerializer,
    DataItemSerializer,
    GetRealDataItemSerializer,
    GetRealDataEntrySerializer,
    RealDataEntrySerializer,
    DiscreteDataItemSerializer,
    DiscreteDataEntrySerializer,
    GetDiscreteDataItemSerializer,
    GetDiscreteDataEntrySerializer,
    GetTopicSerializer,
    TopicSerializer,
    DeviceSerializer,
    GetDeviceSerializer,
    GetDeviceTypeSerializer,
    ServerSerializer,
    GetServerSerializer,
    RestServerSerializer,
    GetRestServerSerializer,
    MqttBrokerSerializer,
    GetMqttBrokerSerializer,
    FunctionSerializer,
    GetFunctionSerializer,
    CommandSerializer,
    GetCommandSerializer,
    )
from automation.models import (
    DataItem,
    RealDataItem,
    RealDataEntry,
    DiscreteDataItem,
    DiscreteDataEntry,
    Topic,
    MqttBroker,
    RestServer,
    Server,
    )

from command.models import (
    Device,
    DeviceType,
    Function,
    Command,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DataItemViewSet(viewsets.ModelViewSet):
    queryset = DataItem.objects.all()
    serializer_class = DataItemSerializer


class RealDataItemViewSet(viewsets.ModelViewSet):
    queryset = RealDataItem.objects.all()
    serializer_class = GetRealDataItemSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetRealDataItemSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return RealDataItemSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class RealDataEntryViewSet(viewsets.ModelViewSet):
    queryset = RealDataEntry.objects.all().order_by('-id')
    serializer_class = GetRealDataEntrySerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetRealDataEntrySerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return RealDataEntrySerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class DiscreteDataItemViewSet(viewsets.ModelViewSet):
    queryset = DiscreteDataItem.objects.all()
    serializer_class = GetDiscreteDataItemSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetDiscreteDataItemSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return DiscreteDataItemSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class DiscreteDataEntryViewSet(viewsets.ModelViewSet):
    queryset = DiscreteDataEntry.objects.all().order_by('-id')
    serializer_class = GetDiscreteDataEntrySerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetDiscreteDataEntrySerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return DiscreteDataEntrySerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class DiscrerteDataEntryViewSet(viewsets.ModelViewSet):
    queryset = DiscreteDataEntry.objects.all().order_by('-id')
    serializer_class = GetRealDataEntrySerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetRealDataEntrySerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return RealDataEntrySerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetTopicSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return TopicSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = GetDeviceSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetDeviceSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return DeviceSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = DeviceType.objects.all()
    serializer_class = GetDeviceTypeSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = GetServerSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetServerSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return ServerSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class RestServerViewSet(viewsets.ModelViewSet):
    queryset = RestServer.objects.all()
    serializer_class = GetRestServerSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetRestServerSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return RestServerSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class MqttBrokerViewSet(viewsets.ModelViewSet):
    queryset = MqttBroker.objects.all()
    serializer_class = GetMqttBrokerSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetMqttBrokerSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return MqttBrokerSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class FunctionViewSet(viewsets.ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = GetFunctionSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetFunctionSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return FunctionSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = GetCommandSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetCommandSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return CommandSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


def function_value(request, **kwargs):
    from command.models import Command, Function
    import json
    import time

    def format_args(arg):
        if not arg:
            return arg
        try:
            f = float(arg)
            i = int(f)
            return i if f == i else f
        except ValueError:
            return arg

    if request.method == 'GET':
        string_args = request.GET.getlist('args[]', '')
        args = list(map(format_args, string_args))
        f = Function.objects.get(id=kwargs['function_id'])
        cmd = Command()
        cmd.function = f
        cmd.args = args
        try:
            commander.run(cmd)
            timeout = time.perf_counter() + cmd.function.response_timeout
            while time.perf_counter() < timeout:
                cmd.refresh_from_db()
                if cmd.executed:
                    data = json.loads(cmd.return_message)
                    return JsonResponse(data, status=200, safe=False)
                else:
                    time.sleep(.5)
                    print("not complete")
            return JsonResponse("We did not get a value ", status=200, safe=False)
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"ret_value": "Error: Check arguments are set."}, status=200, safe=False)
