# Generated by Django 5.0.3 on 2024-04-09 17:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_remove_curso_data_de_criacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudante',
            name='data_nascimento',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
