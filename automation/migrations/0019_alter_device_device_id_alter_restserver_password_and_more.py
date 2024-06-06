# Generated by Django 4.2.6 on 2023-11-27 07:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0018_alter_device_device_id_alter_restserver_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('cae7763e-6794-49d9-b93a-3b9ab4d95a7a'), unique=True),
        ),
        migrations.AlterField(
            model_name='restserver',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restserver',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]