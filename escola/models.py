from django.db import models
from .validators import validar_cpf, validar_nome, validar_celular, validar_email, validar_data_nascimento

class Estudante(models.Model):
    nome = models.CharField(max_length=100, validators=[validar_nome])
    email = models.EmailField(max_length=30, validators=[validar_email])
    cpf = models.CharField(max_length=11, unique=True, validators=[validar_cpf])
    celular = models.CharField(max_length=11, validators=[validar_celular])
    data_nascimento = models.DateField(validators=[validar_data_nascimento])

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, default='B')

    def __str__(self):
        return self.codigo


class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, default='M')
