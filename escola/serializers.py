from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from .validators import validar_cpf, validar_nome, validar_celular, validar_email, validar_data_nascimento

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate(self, dados):
        # As validações já foram feitas no models.py através dos validators, 
        # mas podemos adicionar validações adicionais aqui se necessário.
        
        # Validação extra exemplo: nome não pode ser "admin"
        if dados['nome'].lower() == 'admin':
            raise serializers.ValidationError({'nome': 'O nome não pode ser "admin".'})

        return dados


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_nome']
