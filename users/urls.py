from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterUserView, LoginView


urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginView.as_view(), name='login'),
]
