from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('add/<str:ticker>/', views.stock_indicators, name='stock_indicators'),
    path('details/<str:ticker>/', views.get_details, name='get_details'),
    path('moving-average/<str:ticker>/', views.get_moving_average, name='get_moving_average'),
    path('rsi/<str:ticker>/', views.get_RSI_14, name='get_RSI'),
]
