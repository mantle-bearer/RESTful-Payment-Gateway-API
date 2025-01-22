from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    reference = serializers.CharField(read_only=True)  # Make reference read_only

    class Meta:
        model = Payment
        fields = '__all__'

