from rest_framework.test import APITestCase
from rest_framework import status
from .models import Candle

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

    def test_get_all_candles(self):
        # 1. Create a dummy candle in the test database
        Candle.objects.create(
            symbol="ETH/USDT",
            timeframe="1d",
            open_price="3000.00",
            high_price="3100.00",
            low_price="2950.00",
            close_price="3050.00",
            volume="500.25",
            timestamp="2026-03-10T00:00:00Z"
        )

        # 2. Make a GET request to the list endpoint
        response = self.client.get('/api/candles/')

        # 3. Assert the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 4. Assert that the list contains exactly 1 candle
        self.assertEqual(len(response.data), 1)
        
        # 5. Assert the symbol matches what we created
        self.assertEqual(response.data[0]['symbol'], "ETH/USDT")

    def test_validation_error_high_price_lower_than_low_price(self):
        # Intentional bad data: high_price (60000) < low_price (64100)
        bad_payload = {
            "symbol": "SOL/USDT",
            "timeframe": "1h",
            "open_price": "64500.00",
            "high_price": "60000.00",
            "low_price": "64100.00",
            "close_price": "65000.00",
            "volume": "120.53",
            "timestamp": "2026-03-09T06:00:00Z"
        }
        
        # Make the POST request
        response = self.client.post('/api/candles/', bad_payload, format='json')
        
        # 1. Assert it blocked the creation (400 Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # 2. Assert the specific error message is present
        self.assertIn("price_error", response.data)