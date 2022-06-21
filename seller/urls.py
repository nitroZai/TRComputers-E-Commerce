from django.urls import path
from . import views

urlpatterns = [

    path('productupload/', views.productUpload , name= 'productupload'),
    path('dashboard/', views.dashboard , name= 'dashboard'),

]