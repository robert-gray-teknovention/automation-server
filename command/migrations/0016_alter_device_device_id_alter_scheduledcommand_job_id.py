# Generated by Django 4.2.6 on 2024-03-30 22:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0015_alter_device_device_id_alter_function_device_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('715a5d53-e6b5-462a-a1f5-3192710cf6b1'), unique=True),
        ),
        migrations.AlterField(
            model_name='scheduledcommand',
            name='job_id',
            field=models.CharField(default=uuid.UUID('7abcafbf-4f35-4874-831e-d329ccd9b2a9'), max_length=40),
        ),
    ]