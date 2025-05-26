from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver 

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import random
import string
from django.db.models.signals import post_save
from .models import Referral
from .models import Profile, Property

# from . models import Notification 

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        


# @receiver(post_save,sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.userprofile.save()

@receiver(post_save, sender=User)
def create_referral_code(sender, instance, created, **kwargs):
    if created:
        referral_code = '' .join(random.choices(string.ascii_letters + string.digits, k=6))
        Referral.objects.create(referrer=instance, referral_code=referral_code)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        # Kama profile haipo, tengeneza moja
        Profile.objects.create(user=instance)
