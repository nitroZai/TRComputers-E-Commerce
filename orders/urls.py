from django.urls import path
from .views import *

urlpatterns  = [

    path('ordering/', orderering, name='ordering'),

]