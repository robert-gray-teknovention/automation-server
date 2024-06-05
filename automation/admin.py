from django.contrib import admin
from .models import (
    MqttBroker,
    RestServer,
    DataGroup,
    DataItem,
    RealDataItem,
    StringDataItem,
    DiscreteDataItem,
    IntegerDataItem,
    Topic,
    ComputerFunctionAssigner,
    )


@admin.register(MqttBroker)
class MqttServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'server_type')


@admin.register(RestServer)
class RestServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'server_type')


class DataItemsInLine(admin.TabularInline):
    model = DataItem.data_group.through
    extra = 0


@admin.register(DataGroup)
class DataGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [DataItemsInLine,]


@admin.register(RealDataItem)
class RealDataItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'data_type', 'topic')


@admin.register(DiscreteDataItem)
class DiscreteDataItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'data_type', 'topic')


@admin.register(StringDataItem)
class StringDataItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'data_type', 'topic')


@admin.register(IntegerDataItem)
class IntegerDataItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'data_type', 'topic')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'server')


@admin.register(ComputerFunctionAssigner)
class ComputerFunctionAssignerAdmin(admin.ModelAdmin):
    exclude = ('type',)
    list_display = ('dataitem', 'read_write')
