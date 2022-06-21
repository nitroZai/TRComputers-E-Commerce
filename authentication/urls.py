from django.urls import path
from . import views


urlpatterns = [

    path('register/', views.register, name='register'),
    path('registerSave/', views.registerSave, name='registerSave'),
    path('login/', views.loginn, name='login'),
    path('postLogin/', views.postLogin, name='postLogin'),
    path('logout/', views.logoutt, name='logout'),
    
]