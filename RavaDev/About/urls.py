# About/urls.py
from django.urls import path
from . import views

app_name = 'About'  # Opcjonalnie, ale zalecane dla namespacingu

urlpatterns = [
    path('', views.about, name='about'),
    path("member/<int:member_id>/", views.team_member, name="team_member"),
]