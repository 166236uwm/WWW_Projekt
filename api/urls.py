from django.urls import path
from . import views

urlpatterns = [
    path('userGet', views.getData),
    path('userAdd', views.addUsers),
]