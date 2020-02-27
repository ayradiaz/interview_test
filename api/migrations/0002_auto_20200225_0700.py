# Generated by Django 3.0.3 on 2020-02-25 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name_plural': 'Library'},
        ),
        migrations.AlterModelOptions(
            name='libraryentries',
            options={'verbose_name_plural': 'Library Entries'},
        ),
        migrations.AlterField(
            model_name='library',
            name='active_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='active_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
