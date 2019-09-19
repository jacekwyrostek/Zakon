# Generated by Django 2.2.4 on 2019-09-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mass', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mass',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mass',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
    ]
