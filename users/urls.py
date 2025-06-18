# users/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import register_user, user_list

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', register_user),  # Admin-only
    path('users/', user_list),         # Admin-only list/manage users
]
