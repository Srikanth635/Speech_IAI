# Generated by Django 3.0.4 on 2020-07-28 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0034_auto_20200728_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='omnetppconfigtype',
            old_name='config_has_multiple_instances',
            new_name='has_multiple_instances',
        ),
        migrations.RenameField(
            model_name='omnetppconfigtype',
            old_name='config_label',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='omnetppconfigtype',
            old_name='config_name',
            new_name='name',
        ),
    ]
