# Generated by Django 4.0.4 on 2022-06-08 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='date_appointment',
            new_name='date_joined',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='date_appointment',
            new_name='date_joined',
        ),
    ]
