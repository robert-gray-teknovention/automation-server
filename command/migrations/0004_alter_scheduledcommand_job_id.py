# Generated by Django 4.2.6 on 2024-03-30 06:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0003_alter_scheduledcommand_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledcommand',
            name='job_id',
            field=models.CharField(default=uuid.UUID('4257dd93-163d-4c7b-b6a9-812c5bae1c0f'), max_length=40),
        ),
    ]