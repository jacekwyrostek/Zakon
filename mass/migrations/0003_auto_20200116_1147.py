# Generated by Django 2.2.6 on 2020-01-16 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mass', '0002_auto_20200115_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mass',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mass.Places', verbose_name='Miejsce'),
        ),
        migrations.AlterField(
            model_name='mass',
            name='priest',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, unique_for_date='day', verbose_name='Kapłan'),
        ),
        migrations.AlterField(
            model_name='mass',
            name='startTime',
            field=models.TimeField(verbose_name='Godzina:'),
        ),
        migrations.AlterField(
            model_name='mass',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mass.MassType', verbose_name='Typ'),
        ),
    ]
