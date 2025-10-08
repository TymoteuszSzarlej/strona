from django.urls import path
from . import views 
from .views import projects, project_detail

app_name = 'Projects'  # Opcjonalnie, ale zalecane dla namespacingu

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    ]