# Generated by Django 4.2.6 on 2024-04-01 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0021_alter_scheduledcommand_job_id'),
        ('automation', '0040_remove_dataitem_device_topic_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='functionassigner',
            name='test',
        ),
        migrations.AlterField(
            model_name='topic',
            name='device',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='command.device'),
        ),
    ]
