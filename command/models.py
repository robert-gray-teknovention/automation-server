from django.db import models
import uuid


# Create your models here.


class DeviceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=50)
    device_id = models.UUIDField(default=uuid.uuid4)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        def create_func(name, read_write):
            func = Function()
            func.name = name
            func.read_write = read_write
            func.active = True
            func.args = []
            func.remote = True
            func.asyncro = False
            func.device = self
            func.save()
        if self.functions.filter(name='read_functions', device=self).count() == 0:
            create_func('read_functions', Function.ReadWriteChoices.READ)
        if self.functions.filter(name='write_functions', device=self).count() == 0:
            create_func('write_functions', Function.ReadWriteChoices.WRITE)


class Function(models.Model):

    class ReadWriteChoices(models.IntegerChoices):
        NONE = 0
        READ = 1
        WRITE = 2
    name = models.CharField(max_length=100)
    args = models.JSONField(default=[], blank=True)  # Dictionary of the args and kwargs
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True, related_name='functions')
    remote = models.BooleanField(default=False)
    asyncro = models.BooleanField(default=False)
    response_timeout = models.IntegerField(default=10)
    active = models.BooleanField(default=True)
    read_write = models.IntegerField(default=ReadWriteChoices.NONE, choices=ReadWriteChoices.choices)
    value = 'not queried'

    class Meta:
        unique_together = ('name', 'device')

    def __str__(self):
        return str(self.device) + ' : ' + self.name

    def save(self, *args, **kwargs):
        # self.full_clean()
        if self.args is None:
            self.args = []
        super(Function, self).save(*args, **kwargs)


class ScheduledCommand(models.Model):
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    args = models.JSONField(null=models.CASCADE)
    asyncro = models.BooleanField(default=False)
    job_id = models.UUIDField(default=uuid.uuid4)
    interval_number = models.IntegerField(default=1)
    interval = models.CharField(max_length=20)
    at = models.CharField(max_length=5, null=True)
    run_once = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def run(self):
        cmd = Command()
        cmd.function = self.function
        cmd.args = self.args
        cmd.asyncro = self.asyncro
        cmd.schedule = self
        cmd.run()


class Command(models.Model):
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    schedule = models.ForeignKey(ScheduledCommand, on_delete=models.CASCADE, null=True)
    args = models.JSONField(null=True)  # Dictionary of the values of args
    executed = models.BooleanField(default=False)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    return_message = models.JSONField(null=True)
    # asyncro = models.BooleanField(default=False)
