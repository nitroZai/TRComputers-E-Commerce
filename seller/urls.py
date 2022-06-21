from django.urls import path
from . import views

urlpatterns = [    
    path('dashboard/', views.dashboard , name= 'dashboard'),
    path('productupload/', views.productUpload , name= 'productupload'),
    path('ordersReceived/', views.orders_received, name= 'ordersReceived'),
]