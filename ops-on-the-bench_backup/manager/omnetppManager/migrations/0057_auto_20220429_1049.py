# Generated by Django 3.2.13 on 2022-04-29 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__latest__'),
        ('omnetppManager', '0056_auto_20211027_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
        migrations.AddField(
            model_name='simulation',
            name='sim_server',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.CreateModel(
            name='UserProfileParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='The key for the value', max_length=30)),
                ('value', models.CharField(help_text='The value for the key', max_length=30)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='omnetppManager.userprofile')),
            ],
        ),
    ]
