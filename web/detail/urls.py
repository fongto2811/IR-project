from django.urls import path
from . import views

urlpatterns = [
    path('', views.detail, name='detail'),
]