from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home Page'),
    path('signup/', views.signup, name='signup'),
    path('check_existing_data/', views.check_existing_data,
         name='check_existing_data'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search_donor', views.search_donor, name='search_donor'),

]
