from django.urls import path
from . import views

urlpatterns = [
    path('banks/', views.banks, name='banks')
]
