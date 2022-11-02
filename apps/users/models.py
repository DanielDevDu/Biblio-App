#!/env/bin/python3
"""
------------------------------
Define CustomUserModel class
------------------------------
"""
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# My models
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    ----------------------------------
    Custom User Model with email field
    ----------------------------------
    """
    class Role(models.TextChoices):
        """
        -----------------------
        Define User Types
        -----------------------
        """
        ADMIN = "ADMIN", _("admin")
        LIBRARIAN = "LIBRARIAN", _("librarian")
        READER = "READER", _("reader")

    base_role = Role.READER

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=50)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
    email = models.EmailField(verbose_name=_("Email"), max_length=255, unique=True)

    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)
    is_admin = models.BooleanField(verbose_name=_("Is Admin"), default=False)
    is_staff = models.BooleanField(verbose_name=_("Is Staff"), default=False)
    is_superuser = models.BooleanField(verbose_name=_("Is SuperUser"), default=False)

    date_joined = models.DateTimeField(
        verbose_name=_("Date Joined"), default=timezone.now
    )

    role = models.CharField(max_length = 20, choices = Role.choices, default = Role.READER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "role"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]

    def __str__(self):
        return self.get_full_name

    @property
    def get_full_name(self):
        """
        ------------------------------
        Return the user's full name
        ------------------------------
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def get_short_name(self):
        """
        ------------------------------
        Return the user's short name
        ------------------------------
        """
        return self.username

    def save(self, *args, **kwargs):
        """
        ------------------------------
        Save User Model
        ------------------------------
        """
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)


class LibrarianManager(models.Manager):
    """
    ------------------
    LibrarianManager
    ------------------
    """
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(role = User.Role.LIBRARIAN)
        return queryset

class Librarian(User):
    """
    ------------------------------
    Define Librarian Model
    ------------------------------
    """
    base_role = User.Role.LIBRARIAN

    class Meta:
        verbose_name = _("Librarian")
        verbose_name_plural = _("Librarians")
        ordering = ["-date_joined"]
        proxy = True
    
    objects = LibrarianManager()

    def __str__(self):
        return "Librarian: " + self.get_full_name

    def save(self, *args, **kwargs):
        """
        ------------------------------
        Save User Model
        ------------------------------
        """
        self.is_admin = True
        self.is_staff = True
        return super().save(*args, **kwargs)


class ReaderManager(models.Manager):
    """
    ------------------
    ReaderManager
    ------------------
    """
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(role = User.Role.READER)
        return queryset

class Reader(User):
    """
    ------------------------------
    Define Reader Model
    ------------------------------
    """
    base_role = User.Role.READER

    class Meta: 
        verbose_name = _("Reader")
        verbose_name_plural = _("Readers")
        ordering = ["-date_joined"]
        proxy = True
    
    objects = ReaderManager()

    def __str__(self):
        return "Reader: " + self.get_full_name