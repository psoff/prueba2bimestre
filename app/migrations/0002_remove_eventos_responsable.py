# Generated by Django 3.1.2 on 2020-10-23 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventos',
            name='responsable',
        ),
    ]