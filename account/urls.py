from django.urls import path
from account.views import UserRegistrationView, UserLoginView, UserProfileView, UserPasswordChangeView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('passwordchange/', UserPasswordChangeView.as_view(), name='passwordchange'),
]
