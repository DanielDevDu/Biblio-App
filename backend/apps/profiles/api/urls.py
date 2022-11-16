"""
---------------------
Urls to profiles app.
---------------------
"""
from django.urls import path
from rest_framework import routers

# from .views import (
#     GetProfileAPIView,
#     UpdateProfileView,
#     ReaderProfileViewSet,
# )
from .views import (
    LibrarianProfileViewSet,
    ReaderProfileViewSet,
    UserProfileViewSet
    )


router = routers.SimpleRouter()
router.register('profiles', ProfileUserViewSet, basename='profiles')
router.register('librarians', ProfileLibrarianViewSet, basename='profiles')
router.register('readers', ReaderProfileViewSet, basename='readers')

urlpatterns = [
    # path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    # path("update/<str:username>/", UpdateProfileView.as_view(), name="update_profile"),
] + router.urls
