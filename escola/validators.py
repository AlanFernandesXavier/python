import re
from datetime import datetime
from django.core.exceptions import ValidationError
from validate_docbr import CPF as CPFValidator

# Inicializa o validador de CPF
cpf_validator = CPFValidator()

def validar_cpf(value):
    """Valida se o CPF é válido."""
    if not cpf_validator.validate(value):
        raise ValidationError('CPF inválido.')

def validar_nome(value):
    """Valida se o nome contém apenas letras."""
    if not value.isalpha():
        raise ValidationError('O nome só pode conter letras.')

def validar_celular(value):
    """Valida se o número de celular contém 11 dígitos."""
    if len(value) != 11 or not value.isdigit():
        raise ValidationError('O celular precisa ter 11 dígitos, incluindo o código de área.')

def validar_email(value):
    """Valida se o formato do e-mail é correto."""
    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if not re.match(email_regex, value):
        raise ValidationError('Formato de e-mail inválido.')

def validar_data_nascimento(value):
    """Valida se a data de nascimento não está no futuro."""
    if value > datetime.now().date():
        raise ValidationError('A data de nascimento não pode ser uma data futura.')
