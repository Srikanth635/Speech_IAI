# Generated by Django 3.0 on 2021-10-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0053_omnetppbenchmarkforwarderparameters_param_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='omnetppbenchmarkforwarderparameters',
            name='param_type',
            field=models.IntegerField(choices=[(1, 'FIXED'), (2, 'RANGE'), (3, 'OPTIONS')], default=1),
        ),
    ]
