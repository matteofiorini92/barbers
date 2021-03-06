# Generated by Django 3.2.9 on 2021-11-22 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.barber')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.treatment')),
            ],
        ),
    ]
