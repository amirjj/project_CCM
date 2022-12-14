from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet

# Routers are easy way to automatically determining URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]

        