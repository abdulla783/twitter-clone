# Generated by Django 3.0.5 on 2020-05-30 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200530_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
    ]
