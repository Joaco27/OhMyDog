# Generated by Django 4.2.1 on 2023-06-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0008_cliente_online_alter_turnos_perro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='edad',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='nombre',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='raza',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
