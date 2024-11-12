from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,    # For obtaining access and refresh tokens
    TokenRefreshView,       # For refreshing the access token using the refresh token
)
from .views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # Add JWT endpoints to the URL patterns
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # Login and get tokens
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh the access token
    
    # Include the router-generated URLs for the viewsets
    path('', include(router.urls)),
]