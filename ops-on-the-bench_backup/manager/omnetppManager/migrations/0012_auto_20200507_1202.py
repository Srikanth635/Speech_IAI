# Generated by Django 3.0.4 on 2020-05-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0011_auto_20200507_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='shared_link',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='status',
            field=models.IntegerField(choices=[(1, 'queued'), (2, 'finished'), (3, 'failed'), (4, 'started'), (5, 'deferred'), (6, 'scheduled'), (7, 'unknown'), (8, 'aborted')], default=7),
        ),
    ]
