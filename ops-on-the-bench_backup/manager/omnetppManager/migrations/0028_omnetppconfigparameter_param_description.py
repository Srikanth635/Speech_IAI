# Generated by Django 3.0.4 on 2020-07-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0027_auto_20200727_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='omnetppconfigparameter',
            name='param_description',
            field=models.TextField(default=''),
        ),
    ]
