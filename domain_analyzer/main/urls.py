from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('domain-analyzer/', views.analyze_domain),
]