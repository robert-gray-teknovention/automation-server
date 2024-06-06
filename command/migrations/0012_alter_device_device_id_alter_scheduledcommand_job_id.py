# Generated by Django 4.2.6 on 2024-03-30 07:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0011_alter_device_device_id_alter_scheduledcommand_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('1f511216-ebd2-44ad-81ff-c297718f91dc'), unique=True),
        ),
        migrations.AlterField(
            model_name='scheduledcommand',
            name='job_id',
            field=models.CharField(default=uuid.UUID('16c03267-f737-4e7b-a54e-bac11a75c952'), max_length=40),
        ),
    ]