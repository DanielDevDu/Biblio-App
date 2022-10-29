#!/env/bin/python3
"""
------------------------------
Define Profile class
------------------------------
"""
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# My models
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    """
    --------------
    Gender Options
    --------------
    """

    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")

class ReaderStatus(models.TextChoices):
    """
    ----------------
    Reader Status
    ----------------
    """
    ACTIVE = "ACTIVE", _("Active")
    INACTIVE = "INACTIVE", _("Inactive")
    CANCELED = "CANCELED", _("Canceled")
    SUSPENDED = "SUSPENDED", _("Suspended")

class ReaderProfile(TimeStampedUUIDModel):
    """
    -------------------------------
    Profile Class to Reader User
    -------------------------------
    """
    user = models.OneToOneField(User, related_name="reader_profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+41524204242"
    )
    about_me = models.TextField(
        verbose_name=_("About me"), default="say something about yourself"
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="/profile_default.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("Country"), default="CO", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Medellin",
        blank=False,
        null=False,
    )

    total_books_borrowed = models.IntegerField(
        verbose_name=_("Number of Books Borrowed"), default=0, null=True, blank=True
    )
    current_books_borrowed = models.IntegerField(
        verbose_name=_("Number of Books Borrowed currently"), default=0, null=True, blank=True
    )
    status = models.CharField(
        verbose_name=_("Status"), choices=ReaderStatus.choices, default=ReaderStatus.ACTIVE, max_length=20
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
    
class LibrarianProfile(TimeStampedUUIDModel):
    """
    -------------------------------
    Profile Class to Librarian User
    -------------------------------
    """
    user = models.OneToOneField(User, related_name="librarian_profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+41524204242"
    )
    about_me = models.TextField(
        verbose_name=_("About me"), default="say something about yourself"
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="/profile_default.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("Country"), default="CO", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Medellin",
        blank=False,
        null=False,
    )
    # library  = models.ForeignKey(Library, related_name="librarians", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s profile"
