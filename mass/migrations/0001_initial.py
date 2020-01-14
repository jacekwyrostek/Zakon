# Generated by Django 2.2.6 on 2020-01-14 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MassType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('massType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(null=True, verbose_name='Data:')),
                ('startTime', models.TimeField(unique_for_date='day', verbose_name='Godzina:')),
                ('intention', models.TextField(blank=True, default='Wolny Termin', max_length=250, null=True, verbose_name='Intencja:')),
                ('surname', models.CharField(max_length=50, null=True, verbose_name='Imię i Nazwisko:')),
                ('email', models.EmailField(blank=True, max_length=70, null=True)),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mass.Places')),
                ('priest', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, unique_for_date='startTime')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mass.MassType')),
            ],
            options={
                'ordering': ['day', 'startTime'],
            },
        ),
    ]
