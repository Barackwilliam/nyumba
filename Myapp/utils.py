
from datetime import timedelta
from django.utils.timezone import now
from .models import Profile  # Hakikisha model iko kwenye app yako

def remove_expired_verifications():
    """ Ondoa verification kwa accounts zilizoisha muda """
    expiry_date = now() - timedelta(days=30)
    expired_profiles = Profile.objects.filter(is_verified=True, verified_at__lte=expiry_date)
    
    for profile in expired_profiles:
        profile.is_verified = False
        profile.verified_at = None
        profile.save()
        print(f"Verification removed for {profile.user.username}")
