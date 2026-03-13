from rest_framework import generics
from .models import Candle
from .serializers import CandleSerializer

class CandleListCreateView(generics.ListCreateAPIView):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer

class CandleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer