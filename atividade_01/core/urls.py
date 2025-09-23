from django.urls import path
from . import views  # importa as views do core

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('resposta/', views.resposta, name='resposta'), 
]
