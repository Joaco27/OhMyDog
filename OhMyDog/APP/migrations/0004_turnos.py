# Generated by Django 4.2.1 on 2023-05-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_alter_contactocuidador_telcuidador_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=400)),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('raza', models.CharField(max_length=30)),
            ],
        ),
    ]