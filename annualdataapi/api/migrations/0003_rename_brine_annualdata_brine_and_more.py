# Generated by Django 4.2.1 on 2023-05-24 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_well_annualdata_api_well_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annualdata',
            old_name='BRINE',
            new_name='brine',
        ),
        migrations.RenameField(
            model_name='annualdata',
            old_name='GAS',
            new_name='gas',
        ),
        migrations.RenameField(
            model_name='annualdata',
            old_name='OIL',
            new_name='oil',
        ),
        migrations.RenameField(
            model_name='annualdata',
            old_name='API_WELL_NUMBER',
            new_name='well',
        ),
    ]
