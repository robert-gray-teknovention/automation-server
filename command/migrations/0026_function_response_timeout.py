# Generated by Django 4.2.6 on 2024-04-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0025_alter_function_name_alter_function_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='response_timeout',
            field=models.IntegerField(default=10),
        ),
    ]
