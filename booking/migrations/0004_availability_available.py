# Generated by Django 3.2.9 on 2021-11-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_availability_treatment'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
