# Generated by Django 4.1.7 on 2023-06-17 03:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreC', models.CharField(max_length=15)),
                ('usuario', models.CharField(max_length=30)),
                ('contra', models.CharField(max_length=30, null=True)),
                ('mail', models.EmailField(max_length=30)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactoAdop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('dueño', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=30)),
                ('telUsuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactoCuidador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuidador', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=30)),
                ('telUsuario', models.IntegerField()),
                ('telCuidador', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactoPaseador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paseador', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=30)),
                ('telUsuario', models.IntegerField()),
                ('telPaseador', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactoPerdido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreP', models.CharField(max_length=30)),
                ('telDueño', models.IntegerField()),
                ('encontro', models.CharField(max_length=30)),
                ('telEncontro', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cuidador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('zona', models.CharField(max_length=20)),
                ('disponibilidad', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreP', models.CharField(blank=True, max_length=30, null=True)),
                ('mailD', models.EmailField(blank=True, max_length=30, null=True)),
                ('raza', models.CharField(blank=True, max_length=30, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=400)),
                ('fecha', models.DateField()),
                ('castrado', models.CharField(blank=True, max_length=3, null=True)),
                ('pulsaciones', models.CharField(max_length=30)),
                ('estudios_complementarios', models.CharField(max_length=400)),
                ('diagnostico_presuntivo', models.CharField(max_length=400)),
                ('tratamiento', models.CharField(max_length=400)),
                ('proxima_visita', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paseador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('zona', models.CharField(max_length=20)),
                ('disponibilidad', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('raza', models.CharField(max_length=30)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('peso', models.IntegerField(default=0)),
                ('castrado', models.CharField(default='NO', max_length=2)),
                ('sexo', models.CharField(blank=True, max_length=15, null=True)),
                ('emailDueño', models.EmailField(max_length=30)),
                ('fechaNacimiento', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PerroAdopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('raza', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('zona', models.CharField(default='NO', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PerroPerdido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('dueño', models.CharField(max_length=30)),
                ('telDueño', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('raza', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=30)),
                ('zona', models.CharField(max_length=50)),
                ('fechaD', models.DateTimeField()),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=400)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('raza', models.CharField(blank=True, max_length=30, null=True)),
                ('perro', models.CharField(blank=True, max_length=100, null=True)),
                ('sexo', models.CharField(blank=True, max_length=15, null=True)),
                ('motivo', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('telDueño', models.IntegerField()),
                ('fHoraria', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
