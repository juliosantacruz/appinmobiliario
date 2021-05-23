# Generated by Django 3.2.3 on 2021-05-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='images/paginas', verbose_name='Imagen')),
                ('contenido', models.TextField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
