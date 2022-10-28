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
        # extra_fields.setdefault("is_staff", False)
        # extra_fields.setdefault("is_admin", False)
        # extra_fields.setdefault("is_superuser", False)

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
        extra_fields.setdefault("type", "ADMIN")

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
        superuser.save(using=self._db)
        return

class LibrarianManager(CustomUserManager):
    """
    ------------------
    LibrarianManager
    ------------------
    """

    def create_librarian(
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
        Create and save a Librarian with the given email and password
                            and extra fields.
        --------------------------------------------------------------
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError(_("Librarian must have is_admin=True."))
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Librarian must have is_staff=True."))
        if extra_fields.get("is_superuser") is True:
            raise ValueError(_("Librarian must have is_superuser=False."))

        if not password:
            raise ValueError(_("Librarian must submit a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Librarian Account: An email address is required"))

        # create librarian
        librarian = self.create_user(
            username, first_name, last_name, email, password, **extra_fields
        )
        librarian.save(using=self._db)
        return
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type = "LIBRARIAN")
        return queryset


class ReaderManager(CustomUserManager):
    """
    ------------------
    ReaderManager
    ------------------
    """

    def create_reader(
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
        Create and save a Reader with the given email and password
                            and extra fields.
        --------------------------------------------------------------
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_admin") is True:
            raise ValueError(_("Reader must have is_admin=False."))
        if extra_fields.get("is_staff") is True:
            raise ValueError(_("Reader must have is_staff=False."))
        if extra_fields.get("is_superuser") is True:
            raise ValueError(_("Reader must have is_superuser=False."))

        if not password:
            raise ValueError(_("Reader must submit a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Reader Account: An email address is required"))

        # create reader
        reader = self.create_user(
            username, first_name, last_name, email, password, **extra_fields
        )
        reader.save(using=self._db)
        return

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type = "READER")
        return queryset