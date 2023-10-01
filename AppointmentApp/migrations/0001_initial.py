# Generated by Django 4.2.5 on 2023-10-01 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text="Doctor's Name", max_length=100)),
                ('pincode', models.IntegerField(default=None, help_text='Pincode in which doctor operates')),
                ('start_datetime', models.DateTimeField(default=django.utils.timezone.now, help_text='Start Time When doctor sits in the clinic')),
                ('end_datetime', models.DateTimeField(default=django.utils.timezone.now, help_text='End Time When doctor sits in the clinic')),
                ('booked_slots', models.IntegerField(default=None, help_text='Number of slots already Booked')),
                ('phone_number', models.CharField(default='', help_text="Doctor's Phone Number", max_length=10)),
            ],
            options={
                'verbose_name': 'DoctorsDetail',
                'verbose_name_plural': 'DoctorsDetails',
            },
        ),
        migrations.CreateModel(
            name='PatientBookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text="Patient's Name", max_length=100)),
                ('phone_number', models.CharField(default='', help_text="Patient's Phone Number", max_length=10)),
                ('age', models.IntegerField(default=None, help_text='Age of Patient')),
                ('gender', models.CharField(default='', help_text='Gender of Patient', max_length=10)),
                ('slot_booked', models.IntegerField(default=None, help_text='slot number booked for patient')),
            ],
            options={
                'verbose_name': 'PatientBooking',
                'verbose_name_plural': 'PatientBookings',
            },
        ),
    ]