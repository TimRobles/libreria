# Generated by Django 3.2.12 on 2022-02-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('Apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('Edad', models.IntegerField()),
                ('Pais', models.IntegerField(choices=[(1, 'Perú'), (2, 'Argentina'), (3, 'Colombia'), (4, 'Rusia'), (5, 'Ucrania')], verbose_name='País')),
                ('Profesion', models.CharField(choices=[('Dr', 'Doctor'), ('Ing', 'Ingeniero')], max_length=3, verbose_name='Profesión')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
    ]
