# Generated by Django 3.2.12 on 2022-02-25 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0007_alter_autor_nacimiento'),
        ('editorial', '0004_alter_editorial_slug'),
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='Autor',
            field=models.ManyToManyField(to='autor.Autor'),
        ),
        migrations.AddField(
            model_name='libro',
            name='Editorial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='editorial.editorial'),
            preserve_default=False,
        ),
    ]
