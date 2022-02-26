# Generated by Django 3.2.12 on 2022-02-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('Year', models.IntegerField(verbose_name='Año')),
                ('Paginas', models.IntegerField(verbose_name='Páginas')),
                ('Portada', models.ImageField(upload_to='img/Libro')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
