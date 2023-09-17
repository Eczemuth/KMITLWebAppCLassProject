from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, 
    TokenVerifyView,
)

urlpatterns = [
    path('sign-up', views.EmailRegistrationAPIViews.as_view()), 
    path('sign-in', views.LoginAPIViews.as_view()), 
    path('sign-out', views.LogoutAPIViews.as_view()), 
    path('sign-out/all', views.LogoutAllAPIViews.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()), 
    path('token/generate', TokenObtainPairView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('activate/<str:uidb64>/<str:token>/', views.EmailActivation.as_view(), name='activate'),
    path('reset-password-sender/<str:email>/', views.ResetPasswordSender.as_view()),
    path('reset-password/<str:uidb64>/<str:token>/<str:password>/', views.ResetPassword.as_view(), name='reset-password')
]
