from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, LikeViewSet



router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)   

urlpatterns = [
    path('', include(router.urls)),

 ]
