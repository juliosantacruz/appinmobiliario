# Generated by Django 3.2.3 on 2021-06-08 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0004_asesor_fecha_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
