# Generated by Django 3.1.2 on 2020-10-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('lugar', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('hora', models.CharField(max_length=30)),
                ('responsable', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('encargado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
            ],
        ),
    ]