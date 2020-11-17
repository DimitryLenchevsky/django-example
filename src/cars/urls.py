from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from cars.views import CarCreateView


app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view())
]