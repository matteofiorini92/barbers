# Generated by Django 3.2.9 on 2021-11-18 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barber',
            name='profile_picture_url',
        ),
    ]
