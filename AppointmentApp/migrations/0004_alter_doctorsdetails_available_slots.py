# Generated by Django 4.2.5 on 2023-10-01 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppointmentApp', '0003_doctorsdetails_available_slots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorsdetails',
            name='available_slots',
            field=models.IntegerField(blank=True, default=None, help_text='Number of Patients Doctor Check', null=True),
        ),
    ]