# Generated by Django 2.2.6 on 2020-01-16 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mass', '0006_auto_20200116_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mass',
            name='priest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Kapłan'),
        ),
    ]
