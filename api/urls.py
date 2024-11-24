from django.urls import path
from . import views

urlpatterns = [
    path('userGet', views.getUsers, name='userGet'),
    path('userAdd', views.addUser, name='userAdd'),
    path('productGet', views.getProducts, name='productGet'),
    path('productAdd', views.addProducts, name='productAdd'),
    path('recipeGet', views.getRecipe, name='recipeGet'),
    path('recipeAdd', views.addRecipe, name='recipeAdd'),
    path('transactionGet', views.getTransaction, name='transactionGet'),
    path('transactionAdd', views.addTransaction, name='transactionAdd'),
    path('deliveryGet', views.getDelivery, name='deliveryGet'),
    path('deliveryAdd', views.addDelivery, name='deliveryAdd'),
    path('trnSummary', views.trnSummary, name='trnSummary'),
]