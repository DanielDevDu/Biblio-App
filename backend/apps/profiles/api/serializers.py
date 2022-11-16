"""
----------------------------
Serializers to Profile Model
----------------------------
"""
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from apps.profiles.models import UserProfile, ReaderProfile, LibrarianProfile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    """
    -----------------------------------------
    Class that serialize Reader profile model
    -----------------------------------------
    """

    lookup_field = "id"

    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email", read_only=True)
    country = CountryField(name_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.CharField(source="user.id", read_only=True)
    role = serializers.CharField(source="user.role", read_only=True)
    is_active = serializers.BooleanField(source="user.is_active", read_only=True)

    class Meta:
        model = ReaderProfile
        fields = [
            "id",
            "user_id",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone_number",
            "profile_photo",
            "about_me",
            "gender",
            "country",
            "city",
            "role",
            "is_active",

        ]

    def get_full_name(self, obj):
        """
        -----------------------------
        Get full name from Profile
        -----------------------------
        """
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_reviews(self, obj):
        """
        -----------------------------
        Get reviews from Profile
        -----------------------------
        """
        reviews = obj.agent_review.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # if instance.top_agent:
        #     representation["top_agent"] = True
        return representation

class ReaderProfileSerializer(ProfileSerializer):

    class Meta:
        model = ReaderProfile
        fields = [ 
            "id",
            "user_id",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone_number",
            "profile_photo",
            "about_me",
            "gender",
            "country",
            "city",
            "status",
            "current_books_borrowed",
            "total_books_borrowed",
            "role",
            "is_active"

        ]

class LibrarianProfileSerializer(ProfileSerializer):
    base_model = LibrarianProfile
    class Meta:
        model = LibrarianProfile()
        fields = [
            "id",
            "user_id",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone_number",
            "profile_photo",
            "about_me",
            "gender",
            "country",
            "city",
            "role",

        ]


class UpdateReaderProfileSerializer(serializers.ModelSerializer):
    """
    -----------------------
    Serialize Update method
    -----------------------
    """

    country = CountryField(name_only=True)

    class Meta:
        model = ReaderProfile
        fields = [
            "phone_number",
            "profile_photo",
            "about_me",
            "gender",
            "country",
            "city"
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # if instance.top_agent:
        #     representation["top_agent"] = True
        return representation
