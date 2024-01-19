from django.urls import path 
from .views import myview, abhitnal, mynano

urlpatterns = [
    path('home/', myview ),
    path('abhitnal/', abhitnal, name='abhitnal'),
    path('follow/', mynano), 
]