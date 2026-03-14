from rest_framework import generics, status, serializers
from rest_framework.response import Response
from .models import Candle
from .serializers import CandleSerializer

class CandleListCreateView(generics.ListCreateAPIView):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True) 
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        except serializers.ValidationError as e:
            # 1. Check if our custom "price_error" is in the error dictionary
            if "price_error" in e.detail:
                return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
            
            # 2. If it's not our custom error, it's a missing/invalid field error
            return Response(e.detail, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
        except Exception as e:
            return Response(
                {"error": "An unexpected error occurred while creating the candle."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class CandleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Candle deleted successfully."},
            status=status.HTTP_200_OK
        )
