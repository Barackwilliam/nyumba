
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



# Functions za kuchukua IP na Mkoa
import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

def get_region_by_ip(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        return data.get('region')  # au 'city', au 'country_name'
    except:
        return None
