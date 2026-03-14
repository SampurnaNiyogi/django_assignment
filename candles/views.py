from rest_framework import generics, status
from rest_framework.response import Response
from .models import Candle
from .serializers import CandleSerializer

class CandleListCreateView(generics.ListCreateAPIView):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer

class CandleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer

    def destroy(self, request, *args, **kwargs):
        # Get the object to be deleted
        instance = self.get_object()
        
        # Perform the actual deletion
        self.perform_destroy(instance)
        
        # Return a custom JSON response
        return Response(
            {"message": "Candle deleted successfully."},
            status=status.HTTP_200_OK
        )