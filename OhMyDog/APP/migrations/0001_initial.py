# Generated by Django 4.1.7 on 2023-05-01 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('raza', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
