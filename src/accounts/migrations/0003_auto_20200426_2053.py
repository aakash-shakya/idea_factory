# Generated by Django 3.0 on 2020-04-26 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200426_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
