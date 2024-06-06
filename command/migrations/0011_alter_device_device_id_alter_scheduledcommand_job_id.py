# Generated by Django 4.2.6 on 2024-03-30 07:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0010_alter_device_device_id_alter_scheduledcommand_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('2df6600c-dfdc-4d9a-9711-2eb7471005b2'), unique=True),
        ),
        migrations.AlterField(
            model_name='scheduledcommand',
            name='job_id',
            field=models.CharField(default=uuid.UUID('d467fe50-019d-4186-982b-a36bc5d31935'), max_length=40),
        ),
    ]