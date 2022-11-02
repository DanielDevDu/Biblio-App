from rest_framework import routers, serializers, viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import  UserSerializer, LibrarianSerializer, ReaderSerializer
from .models import Librarian, Reader
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    --------------------------------
    Class that serialize User model
    --------------------------------
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LibrarianViewSet(viewsets.ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = [permissions.AllowAny]


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = [permissions.AllowAny]
