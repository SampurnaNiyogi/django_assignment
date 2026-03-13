from django.db import models

class Candle(models.Model):
    symbol = models.CharField(max_length=20)
    timeframe = models.CharField(max_length=10)
    open_price = models.DecimalField(max_digits=20, decimal_places=8)
    high_price = models.DecimalField(max_digits=20, decimal_places=8)
    low_price = models.DecimalField(max_digits=20, decimal_places=8)
    close_price = models.DecimalField(max_digits=20, decimal_places=8)
    volume = models.DecimalField(max_digits=30, decimal_places=8)
    timestamp = models.DateTimeField()

    class Meta:
        unique_together = ('symbol', 'timeframe', 'timestamp')