from .views import LibrarianProfileViewSet, ReaderProfileViewSet, UserProfileViewSet
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register('users', UserProfileViewSet, basename='users')
router.register('librarians', LibrarianProfileViewSet, basename='librarians')
router.register('readers', ReaderProfileViewSet, basename='readers')

urlpatterns = router.urls