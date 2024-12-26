from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.hello), #main app'indeki main fonksiyonunu main adı ile? dahil etmekte
]