from django.urls import path
from .views import register, login

urlpatterns = [
    path('', login, name='login'),
    path('register', register, name='register'),
]
