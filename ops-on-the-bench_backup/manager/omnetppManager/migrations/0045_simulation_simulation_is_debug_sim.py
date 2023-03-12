# Generated by Django 3.0.4 on 2021-07-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0044_simulation_simulation_state_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='simulation_is_debug_sim',
            field=models.BooleanField(default=False, help_text='Is this a debug simulation? If yes -> ignore for comparison.'),
        ),
    ]