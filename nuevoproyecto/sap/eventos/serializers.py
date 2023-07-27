from rest_framework import serializers


from eventos.models import Tipo, Cliente


class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo
        fields = ['nombre_evento']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'pago', 'direccion']