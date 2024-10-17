# Generated by Django 5.0.3 on 2024-10-17 13:31

import escola.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0005_alter_curso_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='celular',
            field=models.CharField(max_length=11, validators=[escola.validators.validar_celular]),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, validators=[escola.validators.validar_cpf]),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='data_nascimento',
            field=models.DateField(validators=[escola.validators.validar_data_nascimento]),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='email',
            field=models.EmailField(max_length=30, validators=[escola.validators.validar_email]),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='nome',
            field=models.CharField(max_length=100, validators=[escola.validators.validar_nome]),
        ),
    ]
