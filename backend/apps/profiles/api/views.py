from rest_framework import routers, serializers, viewsets, permissions, status
from django.contrib.auth import get_user_model
from .serializers import  ProfileSerializer, ReaderProfileSerializer, LibrarianProfileSerializer, UpdateReaderProfileSerializer
from apps.users.models import Librarian, Reader
from apps.profiles.models import ReaderProfile, LibrarianProfile
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

User = get_user_model()

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    --------------------------------
    Class that serialize User model
    --------------------------------
    """
    queryset = ReaderProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"

    def destroy(self, request, id=None):
        """
        -----------------------------------------
        Dont delete profile, just change property
        is_active of user to false
        -----------------------------------------
        """
        profile = self.queryset.get(id=id)
        if profile:
            profile.user.is_active = False
            profile.user.save()

            return Response({"message": "Profile Deleted Succesfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Profile Not Found"}, status=status.HTTP_404_NOT_FOUND)


class LibrarianProfileViewSet(UserProfileViewSet):
    queryset = LibrarianProfile.objects.all()
    serializer_class = LibrarianProfileSerializer
    permission_classes = [permissions.AllowAny]


class ReaderProfileViewSet(UserProfileViewSet):
    queryset = ReaderProfile.objects.all()
    serializer_class = ReaderProfileSerializer
    permission_classes = [permissions.AllowAny]
