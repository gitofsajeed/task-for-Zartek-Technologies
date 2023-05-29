from django.urls import path, include
from rest_framework import routers
from .views import UserRegistrationViewSet, UserLoginViewSet, UserLogoutViewSet

router = routers.DefaultRouter()
router.register(r'register', UserRegistrationViewSet, basename='user-registration')
router.register(r'login', UserLoginViewSet, basename='user-login')
router.register(r'logout', UserLogoutViewSet, basename='user-logout')



urlpatterns = [
    path('account/', include(router.urls)),
    
]
