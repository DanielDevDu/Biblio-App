#!/env/bin/python3
"""
------------------------------
Define CustomUserManager class
        for Users app
------------------------------
"""
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    -----------------
    CustomUserManager
    -----------------
    """

    def email_validator(self, email: str) -> bool:
        """
        ---------------
        Email validator
        ---------------
        """

        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(
        self,   
        username: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        **extra_fields
    ) -> object:
        """
        --------------------------------------------------------------
        Create and save a User with the given email and password
                            and extra fields.
        --------------------------------------------------------------
        """

        if not username:
            raise ValueError(_("User must submit a username"))
        if not first_name:
            raise ValueError(_("User must submit a first name"))
        if not last_name:
            raise ValueError(_("User must submit a last name"))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))

        # create user
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        # Set password
        user.set_password(password)

        # Extra fields
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superuser", False)

        # Save user
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        username: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        **extra_fields
    ) -> object:
        """
        --------------------------------------------------------------
        Create and save a SuperUser with the given email and password
                            and extra fields.
        --------------------------------------------------------------
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", "ADMIN")

        if extra_fields.get("is_admin") is not True:
            raise ValueError(_("Superuser must have is_admin=True."))
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        if not password:
            raise ValueError(_("Superuser must submit a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin Account: An email address is required"))

        # create superUser
        superuser = self.create_user(
            username, first_name, last_name, email, password, **extra_fields
        )
        superuser.role = "ADMIN"
        superuser.save(using=self._db)
        return super

