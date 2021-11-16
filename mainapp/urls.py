from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skill/', views.skills, name='skills'),
    path('projects/', views.projects, name="projects")
]