"""
--------------------------
Serializers to User Model
--------------------------
"""
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer, UserSerializer as DjoserUserSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from apps.users.models import Librarian, Reader

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')


class UserSerializer(serializers.ModelSerializer):
    """
    --------------------------------
    Class that serialize User model
    --------------------------------
    """

    role_class = "reader"

    gender = serializers.CharField(source="{}_profile.gender".format(role_class))
    phone_number = PhoneNumberField(source="{}_profile.phone_number".format(role_class))
    profile_photo = serializers.ImageField(source="{}_profile.profile_photo".format(role_class))
    city = serializers.CharField(source="{}_profile.city".format(role_class))
    full_name = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "gender",
            "phone_number",
            "profile_photo",
            "city",
            "role"
        ]
        read_only_fields = ["id", "username", "email"]

    def get_full_name(self, obj):
        return self.get_first_name(obj) + " " + self.get_last_name(obj)

    def get_first_name(self, obj):
        return obj.first_name

    def get_last_name(self, obj):
        return obj.last_name
    
    def get_role(self, obj):
        return obj.role

    def to_representation(self, instance):
        """
        -------------------------------------------------------
        Custom representation of the user model serialization
        -------------------------------------------------------
        """
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["is_admin"] = True
        return representation

class LibrarianSerializer(UserSerializer):
    """
    --------------------
    Librarian Serializer
    --------------------
    """

    role_class = "librarian"

    class Meta:
        model = Librarian
        fields = UserSerializer.Meta.fields

class ReaderSerializer(UserSerializer):
    """
    --------------------
    Reader Serializer
    --------------------
    """

    role_class = "reader"
    total_books_borrowed = serializers.IntegerField(source="reader_profile.total_books_borrowed")
    current_books_borrowed = serializers.IntegerField(source="reader_profile.current_books_borrowed")
    status = serializers.CharField(source="reader_profile.status")

    class Meta:
        model = Reader
        fields = UserSerializer.Meta.fields + [
            "total_books_borrowed",
            "current_books_borrowed",
            "status"
        ]
    


class CreateUserSerializer(UserCreateSerializer):
    """
    -------------------------------------------------------
    Class that serialize User model for creation
    -------------------------------------------------------
    """

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password", "role"]

    def validate_role(self, value):
        if value not in ["reader", "librarian"]:
            raise serializers.ValidationError("Role must be either reader or librarian")
        return value
    


class CustomDjoserUserSerializer(DjoserUserSerializer):
    """
    --------------------------------
    Class that serialize User model
    --------------------------------
    """

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "role", "pkid"]
        read_only_fields = ["id", "pkid", "username", "email", "role"]

    def update(self, instance, validated_data):
        """
        ---------------------------------------------
        Custom update method of the user model
        Update the others models of the user
        ---------------------------------------------
        """
        print("IN update from DjsoerUserSerializer")
        return super().update(instance, validated_data)
