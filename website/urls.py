from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fr', views.index_fr, name='index_fr'),
]