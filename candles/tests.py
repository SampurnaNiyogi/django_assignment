from rest_framework.test import APITestCase
from rest_framework import status

class CandleAPITest(APITestCase):
    def test_create_candle(self):
        payload = {
            "symbol": "BTC/USDT",
            "timeframe": "1h",
            "open_price": "64500.00",
            "high_price": "65200.00",
            "low_price": "64100.00",
            "close_price": "65000.00",
            "volume": "120.53",
            "timestamp": "2026-03-09T06:00:00Z"
        }
        response = self.client.post('/api/candles/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)