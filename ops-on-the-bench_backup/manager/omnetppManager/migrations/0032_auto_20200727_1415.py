# Generated by Django 3.0.4 on 2020-07-27 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0031_auto_20200727_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='omnetppconfigtype',
            name='multiple_instances',
            field=models.BooleanField(default=False, help_text='Can this category be used several times in one omnetpp.ini?'),
        ),
        migrations.AlterField(
            model_name='omnetppconfigtype',
            name='name',
            field=models.CharField(help_text='Human readable name for this category', max_length=100),
        ),
    ]
