# Generated by Django 2.0.5 on 2018-07-07 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adults', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adult',
            name='age',
        ),
    ]
