

"""
-----------------------------------
Define Signals to create a Profile
       when user is created
----------------------------------
"""
import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

# My models
from apps.profiles.models import ReaderProfile, LibrarianProfile
from apps.users.models import User
logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "LIBRARIAN":
        LibrarianProfile.objects.create(user=instance)
    if created and instance.role == "READER":
        ReaderProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == "LIBRARIAN":
        instance.librarian_profile.save()
        logger.info(f"{instance}'s profile for Librarian created Succesfully")
    if instance.role == "READER":
        instance.reader_profile.save()
        logger.info(f"{instance}'s profile for Reader created Succesfully")