# Generated by Django 3.2 on 2021-04-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('slug', models.SlugField(max_length=7, unique=True)),
                ('modelo', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('proprietario', models.CharField(max_length=40)),
                ('hora', models.FloatField(max_length=2)),
                ('minutos', models.FloatField(max_length=2)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]