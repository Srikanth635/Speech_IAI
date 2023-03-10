# Generated by Django 3.0 on 2021-08-16 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omnetppManager', '0050_auto_20210805_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='omnetppbenchmarksectionconfig',
            name='section',
        ),
        migrations.RemoveField(
            model_name='omnetppbenchmarksectionparameters',
            name='config',
        ),
        migrations.RemoveField(
            model_name='omnetppbenchmarksubsectionconfig',
            name='enabled_sections',
        ),
        migrations.RemoveField(
            model_name='omnetppbenchmarksubsectionconfig',
            name='subsection',
        ),
        migrations.RemoveField(
            model_name='omnetppbenchmarksubsectionparameters',
            name='config',
        ),
        migrations.DeleteModel(
            name='OmnetppBenchmarkSection',
        ),
        migrations.DeleteModel(
            name='OmnetppBenchmarkSectionConfig',
        ),
        migrations.DeleteModel(
            name='OmnetppBenchmarkSectionParameters',
        ),
        migrations.DeleteModel(
            name='OmnetppBenchmarkSubsection',
        ),
        migrations.DeleteModel(
            name='OmnetppBenchmarkSubsectionConfig',
        ),
        migrations.DeleteModel(
            name='OmnetppBenchmarkSubsectionParameters',
        ),
    ]
