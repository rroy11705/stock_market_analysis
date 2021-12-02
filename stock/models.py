from django.db import models

# Model Tasks 1-5
#####################################

class StockDetails(models.Model):
    
    symbol = models.CharField(max_length=50, primary_key=True, editable=False)
    currency = models.CharField(max_length=20)
    instrument_type = models.CharField(max_length=20)

    def __str__(self):
        return self.symbol


class StockOpen(models.Model):
      
    symbol = models.ForeignKey(StockDetails, on_delete=models.CASCADE)
    timestamp = models.BigIntegerField(default=0)
    value = models.FloatField(max_length=50, default=0)

    def __str__(self):
        return f"{self.timestamp} ({self.symbol})"
    
    
class StockClose(models.Model):
      
    symbol = models.ForeignKey(StockDetails, on_delete=models.CASCADE)
    timestamp = models.BigIntegerField(default=0)
    value = models.FloatField(max_length=50, default=0)

    def __str__(self):
        return f"{self.timestamp} ({self.symbol})"


class StockLow(models.Model):
      
    symbol = models.ForeignKey(StockDetails, on_delete=models.CASCADE)
    timestamp = models.BigIntegerField(default=0)
    value = models.FloatField(max_length=50, default=0)

    def __str__(self):
        return f"{self.timestamp} ({self.symbol})"


class StockHigh(models.Model):
      
    symbol = models.ForeignKey(StockDetails, on_delete=models.CASCADE)
    timestamp = models.BigIntegerField(default=0)
    value = models.FloatField(max_length=50, default=0)

    def __str__(self):
        return f"{self.timestamp} ({self.symbol})"
    
    
class StockVolume(models.Model):
    
    symbol = models.ForeignKey(StockDetails, on_delete=models.CASCADE)
    timestamp = models.BigIntegerField(default=0)
    value = models.FloatField(max_length=50, default=0)

    def __str__(self):
        return f"{self.timestamp} ({self.symbol})"


######################################