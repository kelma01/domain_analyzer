from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('ip-addresses/', views.ip_addresses),
]