# Generated by Django 4.2.6 on 2023-11-27 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0002_rename_mqttserver_mqttbroker'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DataItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('data_type', models.CharField(choices=[('STRING', 'string'), ('DISCRETE', 'discrete'), ('INT', 'integer'), ('REAL', 'real')], max_length=10)),
                ('alarm_enable', models.BooleanField(default=False)),
                ('alarm_status', models.BooleanField(default=False)),
                ('data_group', models.ManyToManyField(to='automation.datagroup')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='devices',
            field=models.ManyToManyField(to='automation.device'),
        ),
        migrations.CreateModel(
            name='DiscreteDataEntry',
            fields=[
                ('dataentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.dataentry')),
                ('value', models.BooleanField(default=False)),
            ],
            bases=('automation.dataentry',),
        ),
        migrations.CreateModel(
            name='DiscreteDataItem',
            fields=[
                ('dataitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.dataitem')),
            ],
            bases=('automation.dataitem',),
        ),
        migrations.CreateModel(
            name='IntegerDataEntry',
            fields=[
                ('dataentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.dataentry')),
                ('value_raw', models.IntegerField(null=True)),
                ('value', models.IntegerField(null=True)),
            ],
            bases=('automation.dataentry',),
        ),
        migrations.CreateModel(
            name='IntegerDataItem',
            fields=[
                ('dataitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.dataitem')),
                ('scaling_on', models.BooleanField()),
                ('lo_scale', models.IntegerField(default=0)),
                ('hi_scale', models.IntegerField(default=100)),
            ],
            bases=('automation.dataitem',),
        ),
        migrations.CreateModel(
            name='RealDataEntry',
            fields=[
                ('dataentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.dataentry')),
                ('decimal_places', models.IntegerField(default=3)),
                ('value', models.FloatField()),
            ],
            bases=('automation.dataentry',),
        ),
        migrations.CreateModel(
            name='RealDataItem',
            fields=[
                ('dataitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.dataitem')),
                ('scaling_on', models.BooleanField()),
                ('lo_scale', models.FloatField(default=0.0)),
                ('hi_scale', models.FloatField(default=100.0)),
                ('decimal_places', models.IntegerField(default=2)),
            ],
            bases=('automation.dataitem',),
        ),
        migrations.CreateModel(
            name='StringDataEntry',
            fields=[
                ('dataentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.dataentry')),
                ('value', models.CharField(max_length=1024)),
            ],
            bases=('automation.dataentry',),
        ),
        migrations.CreateModel(
            name='StringDataItem',
            fields=[
                ('dataitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.dataitem')),
                ('alarm_string', models.CharField(max_length=100)),
            ],
            bases=('automation.dataitem',),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automation.server')),
            ],
        ),
        migrations.AddField(
            model_name='dataitem',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='automation.topic'),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='data_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automation.dataitem'),
        ),
    ]