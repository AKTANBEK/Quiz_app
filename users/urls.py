from django.urls import path, include
from .views import RegisterUserAPIView, UserProfileAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='profile')
]
