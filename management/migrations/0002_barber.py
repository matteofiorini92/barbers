# Generated by Django 3.2.9 on 2021-11-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barber_name', models.CharField(max_length=254)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('start_time', models.TimeField(default='08:00:00')),
                ('end_time', models.TimeField(default='17:00:00')),
            ],
        ),
    ]
