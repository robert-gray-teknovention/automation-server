# Generated by Django 4.2.6 on 2024-03-29 05:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0028_dataitem_read_write_alter_device_device_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('7c3de089-db69-4a24-8fc0-7d352bc8a0a9'), unique=True),
        ),
    ]
