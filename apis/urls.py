from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import (
    UserViewSet,
    DataItemViewSet,
    RealDataItemViewSet,
    RealDataEntryViewSet,
    DiscreteDataItemViewSet,
    DiscreteDataEntryViewSet,
    TopicViewSet,
    DeviceViewSet,
    DeviceTypeViewSet,
    ServerViewSet,
    RestServerViewSet,
    MqttBrokerViewSet,
    FunctionViewSet,
    CommandViewSet,
    function_value,
    )

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'data_items', DataItemViewSet)
router.register(r'real_data_items', RealDataItemViewSet)
router.register(r'real_data_entries', RealDataEntryViewSet)
router.register(r'discrete_data_items', DiscreteDataItemViewSet)
router.register(r'discrete_data_entries', DiscreteDataEntryViewSet)
router.register(r'mqtt_brokers', MqttBrokerViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'device_types', DeviceTypeViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'servers', ServerViewSet)
router.register(r'rest_servers', RestServerViewSet)
router.register(r'functions', FunctionViewSet)
router.register(r'commands', CommandViewSet)

urlpatterns = [
    path('', include(router.urls), name='apis'),
    path('api-auth/', include('rest_framework.urls')),
    path('function/<int:function_id>/value/', function_value, name='function_value')

]
