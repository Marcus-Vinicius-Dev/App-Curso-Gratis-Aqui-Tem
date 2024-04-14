# Generated by Django 5.0.3 on 2024-04-06 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='data_de_criacao',
        ),
        migrations.RemoveField(
            model_name='estudante',
            name='data_nascimento',
        ),
        migrations.AddField(
            model_name='curso',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.categoria'),
            preserve_default=False,
        ),
    ]