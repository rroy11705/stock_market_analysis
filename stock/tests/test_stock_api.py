from django.urls import reverse, resolve
from django.test import SimpleTestCase
from stock.api import views

class ApiUrlsTestCase(SimpleTestCase):
    
    def test_add_stock_indicators_is_resolved(self):
        url = reverse('stock:add_stock_indicators', kwargs={'ticker': 'LTI.NS'})
        self.assertEqual(resolve(url).func, views.stock_indicators)
    
    def test_get_details(self):
        url = reverse('stock:get_details', kwargs={'ticker': 'LTI.NS'})
        self.assertEqual(resolve(url).func, views.get_details)
        
    def test_get_moving_average(self):
        url = reverse('stock:get_moving_average', kwargs={'ticker': 'LTI.NS'})
        self.assertEqual(resolve(url).func, views.get_moving_average)
        
    def test_get_RSI(self):
        url = reverse('stock:get_RSI', kwargs={'ticker': 'LTI.NS'})
        self.assertEqual(resolve(url).func, views.get_RSI_14)
