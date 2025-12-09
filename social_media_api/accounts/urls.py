from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='api_token_auth'),  # returns token on POST with username & password
    path('', include(router.urls)),
]
