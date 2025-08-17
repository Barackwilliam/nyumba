from django.core.management.base import BaseCommand
from Myapp.models import Profile

class Command(BaseCommand):
    help = 'Transfer Cloudinary image URLs to Uploadcare CharFields for Properties and Profiles'

    def handle(self, *args, **kwargs):
        profiles = Profile.objects.all()
        total_profiles = profiles.count()
        self.stdout.write(f"\nFound {total_profiles} profiles. Starting transfer...")

        for index, profile in enumerate(profiles, start=1):
            if profile.profile_picture:
                profile.profile_picture_1 = profile.profile_picture.url
                profile.save()
                self.stdout.write(f"{index}/{total_profiles} - Updated profile for user: {profile.user.username}")
            else:
                self.stdout.write(f"{index}/{total_profiles} - No profile picture to update for user: {profile.user.username}")

        self.stdout.write("\nAll properties and profiles processed successfully.")
