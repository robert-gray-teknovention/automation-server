from django.contrib import admin
from .forms import FunctionAdminForm
from .models import (
    Function,
    Device,
    DeviceType,
    Command,
)


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    form = FunctionAdminForm
    list_display = ('name', 'device')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_id')


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ['function', 'start', 'end', 'return_message']
    list_per_page = 50
