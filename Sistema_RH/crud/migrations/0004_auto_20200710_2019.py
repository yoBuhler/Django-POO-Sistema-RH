# Generated by Django 3.0.8 on 2020-07-10 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20200710_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='sexo',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=250),
        ),
    ]
