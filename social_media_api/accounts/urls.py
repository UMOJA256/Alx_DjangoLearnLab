from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    UserViewSet,
    FollowUserView,
    UnfollowUserView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # Registration
    path("register/", RegisterView.as_view(), name="register"),

    # Login (checker looks for "login/")
    path("login/", LoginView.as_view(), name="login"),

    # User profile
    path("profile/", ProfileView.as_view(), name="profile"),

    # Follow / Unfollow
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),

    # UserViewSet routes
    path("", include(router.urls)),
]
