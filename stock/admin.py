from django.contrib import admin
from . import models

admin.site.register(models.StockDetails)
admin.site.register(models.StockOpen)
admin.site.register(models.StockClose)
admin.site.register(models.StockLow)
admin.site.register(models.StockHigh)
admin.site.register(models.StockVolume)
