from rest_framework import generics, status, serializers
from rest_framework.response import Response
from .models import Candle
from .serializers import CandleSerializer

class CandleListCreateView(generics.ListCreateAPIView):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer

    # Validation Check
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            if isinstance(e, serializers.ValidationError):
                raise e
            return Response(
                {"error": "An unexpected error occurred while creating the candle."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

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