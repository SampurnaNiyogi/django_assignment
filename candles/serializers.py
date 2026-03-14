from rest_framework import serializers
from .models import Candle

class CandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candle
        fields = '__all__'

    def validate(self, data):
        if data.get('high_price') < data.get('low_price'):
            raise serializers.ValidationError({"price_error": "High price cannot be lower than low price."})
        return data