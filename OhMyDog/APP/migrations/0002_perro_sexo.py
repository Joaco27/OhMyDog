# Generated by Django 4.2.1 on 2023-06-12 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='sexo',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
