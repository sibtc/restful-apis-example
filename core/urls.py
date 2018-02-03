from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('github/', views.github, name='github'),
    path('github/client/', views.github_client, name='github_client'),
    path('oxford/', views.oxford, name='oxford'),
]
