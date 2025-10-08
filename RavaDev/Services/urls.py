from django.urls import path
from . import views 
from .views import service_detail, services

app_name = 'Services'  # Opcjonalnie, ale zalecane dla namespacingu

urlpatterns = [
    path('', views.services, name='services'),
    path('<int:service_id>/', views.service_detail, name='service_detail'),
    ]