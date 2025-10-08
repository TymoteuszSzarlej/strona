from django.urls import path
from . import views 

app_name = 'Blog'  # Opcjonalnie, ale zalecane dla namespacingu

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('post/<int:post_id>/', views.post, name='post'),
]