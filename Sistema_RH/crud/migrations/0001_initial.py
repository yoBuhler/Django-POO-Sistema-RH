# Generated by Django 3.0.8 on 2020-07-10 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('pausa_cafe', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('sexo', models.CharField(max_length=250)),
                ('data_nascimento', models.DateField()),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Setor')),
            ],
        ),
    ]
