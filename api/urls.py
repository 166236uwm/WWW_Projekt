from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('userGet', views.getUsers, name='userGet'),
    path('userAdd', views.addUser, name='userAdd'),
    path('userDel', views.deleteUser, name='userDel'),
    path('userUpdt', views.updateUser, name='userUpdate'),
    path('productGet', views.getProducts, name='productGet'),
    path('productAdd', views.addProducts, name='productAdd'),
    path('productDel', views.deleteProduct, name='productDel'),
    path('productUpdt', views.updateProduct, name='productUpdt'),
    path('recipeGet', views.getRecipe, name='recipeGet'),
    path('recipeAdd', views.addRecipe, name='recipeAdd'),
    path('recipeDel', views.deleteRecipe, name='recipeDel'),
    path('recipeUpdt', views.updateRecipe, name='recipeUpdt'),
    path('transactionGet', views.getTransaction, name='transactionGet'),
    path('transactionAdd', views.addTransaction, name='transactionAdd'),
    path('transactionDel', views.deleteTransaction, name='transactionDel'),
    path('transactionUpdt', views.updateTransaction, name='transactionUpdt'),
    path('deliveryGet', views.getDelivery, name='deliveryGet'),
    path('deliveryAdd', views.addDelivery, name='deliveryAdd'),
    path('deliveryDel', views.deleteDelivery, name='deliveryDel'),
    path('deliveryUpdt', views.updateDelivery, name='deliveryUpdt'),
    path('trnSummary', views.trnSummary, name='trnSummary'),
    path('productUsageSummary', views.productUsageSummary, name='productUsageSummary'),
    path('registerUser/', views.UserRegistrationView.as_view(), name='register'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Endpoint do odświeżania tokenu
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
