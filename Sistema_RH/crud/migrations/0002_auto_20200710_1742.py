# Generated by Django 3.0.8 on 2020-07-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='sexo',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=250),
        ),
    ]
