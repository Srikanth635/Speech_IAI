# Generated by Django 3.0.4 on 2020-04-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0007_simulation_notification_mail_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageBackend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backend_name', models.CharField(max_length=100)),
            ],
        ),
    ]
