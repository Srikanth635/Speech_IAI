# Generated by Django 3.0 on 2021-08-05 18:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0046_simulation_terminated'),
    ]

    operations = [
        migrations.CreateModel(
            name='OmnetppBenchmarkSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Sections available on the omnetppbenchmark ini file', max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')])),
                ('label', models.CharField(default='<undefined>', help_text='has it is in the Omnetpp Benchmark ini file without the square brackets', max_length=100, unique=True)),
                ('order', models.IntegerField(default=10, help_text='Order the fields manually. Lower number = higher priority', unique=True)),
            ],
            options={
                'ordering': ('order', '-pk'),
            },
        ),
        migrations.CreateModel(
            name='OmnetppBenchmarkSectionConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_name', to='omnetppManager.OmnetppBenchmarkSection')),
            ],
            options={
                'ordering': ('section__order', '-section__pk', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='OmnetppBenchmarkSubsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Subsections available on the omnetppbenchmark ini file, layers, mobility etc', max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')])),
                ('label', models.CharField(default='<undefined>', max_length=100, unique=True)),
                ('user_selection_enabled', models.BooleanField(default=False, help_text='does this config type allow user select instances of their choice? ')),
                ('order', models.IntegerField(default=10, help_text='Order the fields manually. Lower number = higher priority', unique=True)),
            ],
            options={
                'ordering': ('order', '-pk'),
            },
        ),
        migrations.CreateModel(
            name='OmnetppBenchmarkSubsectionConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('enabled_sections', models.ManyToManyField(to='omnetppManager.OmnetppBenchmarkSection')),
                ('subsection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsection_name', to='omnetppManager.OmnetppBenchmarkSubsection')),
            ],
            options={
                'ordering': ('subsection__order', '-subsection__pk', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='OmnetppBenchmarkSubsectionParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_name', models.CharField(max_length=100)),
                ('param_default_value', models.CharField(max_length=100)),
                ('param_unit', models.CharField(blank=True, default='', max_length=10)),
                ('user_editable', models.BooleanField(default=False)),
                ('param_description', models.CharField(blank=True, default='', max_length=400)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SubsectionParameters', to='omnetppManager.OmnetppBenchmarkSubsectionConfig')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='OmnetppBenchmarkSectionParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_name', models.CharField(max_length=100)),
                ('param_default_value', models.CharField(max_length=100)),
                ('param_unit', models.CharField(blank=True, default='', max_length=10)),
                ('user_editable', models.BooleanField(default=False)),
                ('param_description', models.CharField(blank=True, default='', max_length=400)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SectionParameters', to='omnetppManager.OmnetppBenchmarkSectionConfig')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
