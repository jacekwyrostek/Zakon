# Generated by Django 2.2.4 on 2019-09-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Data Mszy')),
                ('startTime', models.TimeField(help_text='Godzina')),
                ('intention', models.TextField(blank=True, help_text='Intencja Mszy Św.', null=True)),
                ('surname', models.CharField(help_text='Imię i Nazwisko zamawiającego', max_length=50)),
            ],
        ),
    ]
