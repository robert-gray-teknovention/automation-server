# Generated by Django 4.2.6 on 2024-03-30 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0013_alter_device_device_id_alter_scheduledcommand_job_id'),
        ('automation', '0039_dataitem_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataitem',
            name='device',
        ),
        migrations.AddField(
            model_name='topic',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='command.device'),
        ),
    ]
