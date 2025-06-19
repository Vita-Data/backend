# users/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import register_user, user_list, MyTokenObtainPairView
urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', register_user),
    path('users/', user_list),
]