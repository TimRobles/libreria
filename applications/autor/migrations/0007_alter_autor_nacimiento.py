# Generated by Django 3.2.12 on 2022-02-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0006_auto_20220225_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='Nacimiento',
            field=models.DateField(),
        ),
    ]
