from django.urls import path
from . import views 

app_name = 'Contact'

urlpatterns = [
    path('', views.contact, name='contact'),  # Główny kontakt
    path('service/<int:service_id>/', views.contact, name='contact_service'),  # Kontakt z usługą
    path('success/', views.contact_success, name='contact_success'),
]