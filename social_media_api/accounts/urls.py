from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView,
    UserViewSet,
    FollowUserView,
    UnfollowUserView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # Registration
    path("register/", RegisterView.as_view(), name="register"),

    # Follow / Unfollow (GenericAPIView requirements)
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),

    # User viewset (profiles, follow actions, me profile)
    path("", include(router.urls)),
]
