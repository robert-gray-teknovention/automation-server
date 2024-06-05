# Generated by Django 4.2.6 on 2024-03-30 22:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0017_alter_device_device_id_alter_function_args_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('4b92a5b9-d8fe-4cdf-9d38-fd973635c8b4'), unique=True),
        ),
        migrations.AlterField(
            model_name='function',
            name='args',
            field=models.JSONField(blank=True, default=[], null=True),
        ),
        migrations.AlterField(
            model_name='scheduledcommand',
            name='job_id',
            field=models.CharField(default=uuid.UUID('7f15d894-8987-4909-8636-ec9bf3ba1b41'), max_length=40),
        ),
    ]
