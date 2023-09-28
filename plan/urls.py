from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


app_name = "plan"

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/profile/', views.lk, name='lk'),
    path('register/', views.register, name='register'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    ]
