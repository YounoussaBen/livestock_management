from django.urls import include, path
from rest_framework import routers
from authentication.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),  # Use path, not r'^rest-auth/'
]