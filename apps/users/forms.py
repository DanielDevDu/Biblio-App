#!/env/bin/python3
"""
------------------------------
Define Forms for Users app
Form to create Users
------------------------------
"""
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    -----------------------------
    From to create a new user
    -----------------------------
    """

    class Meta(UserCreationForm):
        model = User
        fields = ["email", "first_name", "last_name", "username", "type"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    """
    ------------------------------
    Form to chenge or update a old
                User
    ------------------------------
    """

    class Meta(UserCreationForm):
        model = User
        fields = ["email", "first_name", "last_name", "username"]
        error_class = "error"

class CustomLibrarianCreationForm(UserCreationForm):
    """
    ------------------------------
    From to create a new Librarian
    ------------------------------
    """

    class Meta(UserCreationForm):
        model = User
        fields = ["email", "first_name", "last_name", "username", "type"]
        error_class = "error"