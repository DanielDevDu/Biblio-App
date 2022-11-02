from apps.users.views import LibrarianViewSet, ReaderViewSet, UserViewSet
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('librarians', LibrarianViewSet, basename='librarians')
router.register('readers', ReaderViewSet, basename='readers')


urlpatterns = router.urls