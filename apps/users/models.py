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
from .managers import CustomUserManager, LibrarianManager, ReaderManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    ----------------------------------
    Custom User Model with email field
    ----------------------------------
    """
    class Types(models.TextChoices):
        """
        -----------------------
        Define User Types
        -----------------------
        """
        ADMIN = "ADMIN", _("admin")
        LIBRARIAN = "LIBRARIAN", _("librarian")
        READER = "READER", _("reader")

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

    is_librarian = models.BooleanField(verbose_name=_("Is Librarian"), default=False)
    is_reader = models.BooleanField(verbose_name=_("Is Reader"), default=False)

    date_joined = models.DateTimeField(
        verbose_name=_("Date Joined"), default=timezone.now
    )

    type = models.CharField(max_length = 20, choices = Types.choices, default = Types.READER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username

    @property
    def full_name(self):
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

class Librarian(User):
    """
    ------------------------------
    Define Librarian Model
    ------------------------------
    """
    class Meta:
        verbose_name = _("Librarian")
        verbose_name_plural = _("Librarians")
        ordering = ["-date_joined"]
        proxy = True

    objects = LibrarianManager()

    def save(self, *args, **kwargs):
        """
        ------------------------------
        Save Librarian Model
        ------------------------------
        """
        self.is_librarian = True
        self.type = User.Types.LIBRARIAN
        return super().save(*args, **kwargs)


class Reader(User):
    """
    ------------------------------
    Define Reader Model
    ------------------------------
    """

    class Meta:
        verbose_name = _("Reader")
        verbose_name_plural = _("Readers")
        ordering = ["-date_joined"]
        proxy = True

    objects = ReaderManager()

    def save(self, *args, **kwargs):
        """
        ------------------------------
        Save Reader Model
        ------------------------------
        """
        self.is_reader = True
        self.type = User.Types.READER
        return super().save(*args, **kwargs)