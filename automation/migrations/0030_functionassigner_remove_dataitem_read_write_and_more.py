# Generated by Django 4.2.6 on 2024-03-30 06:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0004_alter_scheduledcommand_job_id'),
        ('automation', '0029_alter_device_device_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionAssigner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('COMPUTER DEVICE', 'ComputerFunctionAssigner'), ('PLC', 'PLCFunctionAssigner')], max_length=50)),
                ('read_write', models.IntegerField(choices=[(0, 'None'), (1, 'Read'), (2, 'Write'), (3, 'Read Write')], default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='dataitem',
            name='read_write',
        ),
        migrations.AlterField(
            model_name='dataitem',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('0d5bee20-1644-414b-b60e-2058a3198f67'), unique=True),
        ),
        migrations.AddField(
            model_name='dataitem',
            name='function_assigner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='automation.functionassigner'),
        ),
        migrations.CreateModel(
            name='ComputerFunctionAssigner',
            fields=[
                ('functionassigner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.functionassigner')),
                ('function_read', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='read_functions', to='command.function')),
                ('function_write', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='write_functions', to='command.function')),
            ],
            bases=('automation.functionassigner',),
        ),
    ]
