from django.urls import path
from .views import CandleListCreateView, CandleRetrieveUpdateDestroyView

urlpatterns = [
    path('candles/', CandleListCreateView.as_view(), name='candle-list-create'),
    path('candles/<int:pk>/', CandleRetrieveUpdateDestroyView.as_view(), name='candle-detail'),
]