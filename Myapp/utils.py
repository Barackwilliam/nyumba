
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




from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_lat_lon(location_name):
    """
    Use Geopy to get latitude and longitude for the location name.
    """
    geolocator = Nominatim(user_agent="myGeocoder")
    
    try:
        location = geolocator.geocode(location_name)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None  # Location not found
    except GeocoderTimedOut:
        return None, None  # Handle timeout, return None
