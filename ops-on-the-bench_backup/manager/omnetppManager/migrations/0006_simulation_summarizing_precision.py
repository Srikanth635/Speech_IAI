# Generated by Django 3.0.4 on 2020-04-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0005_simulation_handled_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='summarizing_precision',
            field=models.FloatField(default=100),
        ),
    ]
