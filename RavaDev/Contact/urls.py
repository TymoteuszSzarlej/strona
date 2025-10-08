from django.urls import path
from . import views 
from .views import contact, contact_success

app_name = 'Contact'  # Opcjonalnie, ale zalecane dla namespacingu

urlpatterns = [
    path('', views.contact, name='contact'),
    path('success/', views.contact_success, name='contact_success'),
]