# Generated by Django 4.2.1 on 2023-05-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_remove_perroadopcion_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='emailDueño',
            field=models.EmailField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
