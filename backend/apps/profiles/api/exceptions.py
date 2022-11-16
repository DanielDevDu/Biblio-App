"""
---------------------------
Exception to Profiles app.
---------------------------
"""
from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    """
    ----------------------------
    Profile not found exception.
    ----------------------------
    """

    status_code = 404
    default_detail = "Profile not found or does not exist."


class NotYourProfile(APIException):
    """
    ----------------------------
    Not your profile exception.
    ----------------------------
    """

    status_code = 403
    default_detail = (
        "You are not allowed to perform this action. This not your profile."
    )
