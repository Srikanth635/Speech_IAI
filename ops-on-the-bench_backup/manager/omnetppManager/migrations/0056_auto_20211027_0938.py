# Generated by Django 3.0 on 2021-10-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0055_omnetppbenchmarkforwarderparameters_param_user_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='omnetppbenchmarkforwarderparameters',
            name='user_editable',
        ),
        migrations.AlterField(
            model_name='omnetppbenchmarkforwarderparameters',
            name='param_user_option',
            field=models.CharField(default='None', help_text='users allowed options if not fixed, entered as a list', max_length=100),
        ),
    ]
