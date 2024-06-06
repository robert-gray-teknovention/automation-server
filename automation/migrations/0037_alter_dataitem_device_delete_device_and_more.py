# Generated by Django 4.2.6 on 2024-03-30 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0010_alter_device_device_id_alter_scheduledcommand_job_id'),
        ('automation', '0036_functionassigner_test_alter_device_device_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataitem',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='command.device'),
        ),
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.DeleteModel(
            name='DeviceType',
        ),
    ]