# Generated by Django 4.2.6 on 2024-03-30 06:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0031_alter_device_device_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('310650a0-d93f-4711-b753-d63579fd10ad'), unique=True),
        ),
    ]
