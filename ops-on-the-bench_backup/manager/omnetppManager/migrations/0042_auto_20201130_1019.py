# Generated by Django 3.0.4 on 2020-11-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0041_auto_20201130_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverconfig',
            name='server_id',
            field=models.SlugField(help_text='The server ID, has to be unique', max_length=30, unique=True),
        ),
    ]
