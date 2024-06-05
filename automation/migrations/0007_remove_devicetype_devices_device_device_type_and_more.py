# Generated by Django 4.2.6 on 2023-11-27 05:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0006_dataitem_device_alter_device_device_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicetype',
            name='devices',
        ),
        migrations.AddField(
            model_name='device',
            name='device_type',
            field=models.ManyToManyField(to='automation.devicetype'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('ce484f49-caf9-43ad-8065-dad5bd38535a'), unique=True),
        ),
    ]
