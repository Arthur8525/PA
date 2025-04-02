from rest_framework import serializers
from .models import Pagamento

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'  #Inclui todos os campos do modelo no JSON