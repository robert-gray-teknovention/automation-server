# import serializer from rest_framework
from rest_framework import serializers
import json
from django.contrib.auth.models import User
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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = 'url', 'id', 'first_name', 'last_name', 'email'


class DataItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataItem
        fields = 'url', 'id', 'name', 'device', 'topic'


class RealDataItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealDataItem
        fields = '__all__'


class GetRealDataItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RealDataItem
        fields = '__all__'


class RealDataEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = RealDataEntry
        fields = '__all__'


class GetRealDataEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RealDataEntry
        fields = '__all__'


class DiscreteDataItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscreteDataItem
        fields = '__all__'


class GetDiscreteDataItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscreteDataItem
        fields = '__all__'


class DiscreteDataEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscreteDataEntry
        fields = '__all__'


class GetDiscreteDataEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscreteDataEntry
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class GetTopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = '__all__'


class GetFunctionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Function
        fields = '__all__'


class GetDeviceSerializer(serializers.HyperlinkedModelSerializer):
    functions = FunctionSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = '__all__'


class GetDeviceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceType
        fields = '__all__'


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'


class GetServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'


class RestServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestServer
        fields = '__all__'


class GetRestServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestServer
        fields = '__all__'


class MqttBrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MqttBroker
        fields = '__all__'


class GetMqttBrokerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MqttBroker
        fields = '__all__'


class CommandSerializer(serializers.ModelSerializer):
    return_message = serializers.JSONField()

    def to_representation(self, instance):
        core_repr = super().to_representation(instance)
        core_repr["return_message"] = json.loads(core_repr["return_message"])
        return core_repr

    class Meta:
        model = Command
        fields = '__all__'


class GetCommandSerializer(serializers.HyperlinkedModelSerializer):
    return_message = serializers.JSONField()

    def to_representation(self, instance):
        core_repr = super().to_representation(instance)
        core_repr["return_message"] = json.loads(core_repr["return_message"])
        return core_repr

    class Meta:
        model = Command
        fields = '__all__'
