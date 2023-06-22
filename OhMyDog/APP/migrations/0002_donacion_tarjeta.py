# Generated by Django 4.1.7 on 2023-06-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('causa', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=50)),
                ('objetivo', models.IntegerField()),
                ('recaudado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('numero', models.IntegerField()),
                ('mesV', models.IntegerField()),
                ('añoV', models.IntegerField()),
                ('saldo', models.IntegerField()),
                ('codigo', models.IntegerField()),
            ],
        ),
    ]
