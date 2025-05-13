from django.db import models
# from cloudinary_storage.storage import MediaCloudinaryStorage
from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError

# from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from datetime import timedelta
from django.utils.timezone import now
from django.utils.text import slugify


from django.template.defaultfilters import slugify
from django.urls import reverse


    

# def validate_video_size(value):
#     limit = 15 * 1024 * 1024
#     if value.size > limit:
#         raise ValidationError('Video File is too large. Size should not Exceed 15MB.')


class Referral(models.Model):
    referrer = models.ForeignKey(User, related_name='referrals', on_delete=models.CASCADE)
    referred_user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='referred_by')
    referral_code = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    rewarded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.referrer.username} code {self.referral_code}"




class Property(models.Model):
    STATUS_CHOICES =('For Rent','For Rent'),('For Sale','For Sale')
    P_STATUS_CHOICES =('Active','Active'),('Sold','Sold')
    MKOA = [('Arusha','Arusha'), ('Dar es salaam','Dar es salaam'), ('Dooma','Dodoma'), ('Ruvuma','Ruvuma'), ('Tabora','Tabora'), ('Mbeya','Mbeya'), ('Morogoro','Morogoro'), ('Lindi','Lindi'), ('Kigoma','Kigoma'),( 'Katavi','Katavi'),('Geita','Geita'), ('Manyara','Manyara'), ('Kilimanjaro','Kilimanjaro'), ('Mara','Mara'), ('Mtwara','Mtwara'), ('Mwanza','Mwanza'), ('Njombe','Njombe'), ('Songwe','Songwe'), ('Tanga','Tanga'), ('Shinyanga','Shinyanga'), ('Iringa','Iringa'), ('Kagera','Kagera'), ('Pemba Kaskazini','Pemba Kaskazini'), ('Pemba Kusini','Pemba Kusini'), ('Pwani','Pwani'),('Rukwa','Rukwa'),('Singida','Singida'),('Simiyu','Simiyu'), ('Zanzibar Kaskazini','Zanzibar Kaskazini'), ('Zanzibar Kusini','Zanzibar Kusini'),('Zanzibar Mjini Magharibi','Zanzibar Mjini Magharibi')]
    PROPERTY_TYPES = [('Apartment','Apartment'), ('House','House'),('Commercial','Commercial')]
    # name = models.CharField(max_length=10)

    title = models.CharField(max_length=255)
    #slug = models.SlugField(unique=True, blank=True)  # Add slug field

    description = models.TextField()
    price = models.IntegerField()
    #bookmarks = models.ManyToManyField(User, related_name="bookmarked_properties", blank=True)
    status = models.CharField(max_length=30,choices=STATUS_CHOICES)
    p_status = models.CharField(max_length=30,choices=P_STATUS_CHOICES)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    country = models.CharField(max_length=25, default='Tanzania')
    region = models.CharField(max_length=30, choices=MKOA)
    district = models.CharField(max_length=30)
    ward = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    #rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    viewers = models.ManyToManyField(User, related_name='viewed_properties', blank=True)
    view_count = models.IntegerField(default=0)
    business_phone = models.CharField(max_length=13)
    business_email = models.EmailField(max_length=60)
    #kitchen = models.IntegerField()

    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    house_size = models.IntegerField()
    nearby = models.TextField()
    image = CloudinaryField('image')
    image1 = CloudinaryField('image')
    image2 = CloudinaryField('image')
    image3 = CloudinaryField('image')
    property_owner = CloudinaryField('image')
    # video = models.FileField(upload_to='property_video/',validators=[validate_video_size], blank=True, null=True default=)
    video_link = models.URLField(max_length=300, blank=True, null=True)
   





    def add_view(self,user):
        if user not in self.viewers.all():
            self.viewers.add(user)
            self.view_count +=1
            self.save()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/property/{self.id}/"
    

class ChatMessage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.receiver} at {self.timestamp}'



class Review(models.Model):
    # property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(default=0)


class Profile(models.Model):
    ROLE_CHOICE = [
        ('owner', 'Owner'),
        ('customer', 'Customer')
    ]
    points = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, default='customer')
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=250, blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)  # Profile picture as optional
    verified_at = models.DateTimeField(null=True, blank=True)  # Tarehe ya kuthibitishwa

    is_verified = models.BooleanField(default=False)  # Field mpya ya verification
    subscription_plan = models.CharField(
        max_length=10,
        choices=[('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum')],
        default='silver') # Default ni Silver
    # profile_completed = models.BooleanField(default=False)  # Field to check if profile is complete


    
    def days_remaining(self):
        """Hesabu siku zilizobaki kabla ya verification ku-expire"""
        if self.is_verified and self.verified_at:
            expiry_date = self.verified_at + timedelta(days=30)
            remaining = (expiry_date - now()).days
            return max(0, remaining)  
        return 0


    
    def save(self, *args, **kwargs):
        """ Ikiwa is_verified inakuwa True, hifadhi tarehe ya sasa """
        if self.is_verified and not self.verified_at:
            self.verified_at = datetime.now()
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.user.username} Profile'







class PopularPlace(models.Model):
    name_of_place = models.CharField(max_length=50)
    number_of_property = models.IntegerField()
    image_of_place = CloudinaryField('image')

    def __str__(self):
        return self.name_of_place
    



class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    offer_image = CloudinaryField('image')
    slug = models.SlugField(unique=True, blank=True,null=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_facebook_share_link(self):
        return f"https://www.facebook.com/sharer/sharer.php?u={reverse('offer_detail', args=[self.slug])}"

    def get_whatsapp_share_link(self):
        return f"https://api.whatsapp.com/send?text={reverse('offer_detail', args=[self.slug])}"

    def get_instagram_share_link(self):
        return reverse('offer_detail', args=[self.slug])

    def get_linkedin_share_link(self):
        return f"https://www.linkedin.com/sharing/share-offsite/?url={reverse('offer_detail', args=[self.slug])}"

    def __str__(self):
        return self.title

 






class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Transaction_image = CloudinaryField('image')
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Myapp_payment'
    def __str__(self):
        return f" Payment by {self.user.username}"




class Featured(models.Model):
    f_property_name = models.OneToOneField(Property, related_name="featured_properties", on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_property_name.title

class PopularProperty(models.Model):
    p_property_name = models.OneToOneField(Property, related_name="popular_properties", on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.p_property_name.title     

class Agent(models.Model):
    jina = models.CharField(max_length=50)
    Cheo = models.CharField(max_length=50)
    image_of_agent = CloudinaryField('image')
    facebook_link = models.URLField(max_length=300, blank=True, null=True)
    twitter_link = models.URLField(max_length=300, blank=True, null=True)
    instagram_link = models.URLField(max_length=300, blank=True, null=True)
    linkedIn = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self. jina

class Partner(models.Model):
    jina = models.CharField(max_length=50)
    image_of_partners = CloudinaryField('image')

    def __str__(self):
        return self.jina





class Client(models.Model):
    name = models.CharField(max_length=50)  
    client_image = CloudinaryField('image')
    location = models.CharField(max_length=50)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self. name





class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inquiries")
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inquiry from {self.full_name} for {self.property.title}'
    




# class PropertyLocation(models.Model):
#     property = models.OneToOneField('Property', on_delete=models.CASCADE, related_name='location')
#     lat = models.FloatField()
#     lon = models.FloatField()

#     def __str__(self):
#         return f"{self.property.title} - ({self.lat}, {self.lon})"
    
    

from .utils import get_lat_lon  # Import the function

class PropertyLocation(models.Model):
    property = models.OneToOneField('Property', on_delete=models.CASCADE, related_name='location')
    lat = models.FloatField(null=True, blank=True)  # Add null=True and blank=True for optional lat/lon
    lon = models.FloatField(null=True, blank=True)  # Add null=True and blank=True for optional lat/lon

    def save(self, *args, **kwargs):
        # Fetch lat/lon based on region, district, or ward
        if not self.lat or not self.lon:
            # Get latitude and longitude based on region name, district name, or ward name
            location_name = f"{self.property.region}, {self.property.district}, {self.property.ward}"
            lat, lon = get_lat_lon(location_name)  # Fetch lat, lon from geocoding API
            
            if lat and lon:  # If geocoding is successful, set the lat/lon
                self.lat = lat
                self.lon = lon
        
        super().save(*args, **kwargs)  # Save the object after updating lat/lon

    def __str__(self):
        return f"{self.property.title} - ({self.lat}, {self.lon})"



class Help_Question(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Hii itaongeza timestamp kwa rekodi mpya


    def __str__(self):
        return self.question





class Holiday(models.Model):
    HOLIDAY_TYPES = (
        ('national', 'National'),
        ('religious', 'Religious'),
    )

    name = models.CharField(max_length=255)
    date = models.DateField()
    type = models.CharField(max_length=20, choices=HOLIDAY_TYPES)
    country = models.CharField(max_length=100, default='Tanzania')

    def __str__(self):
        return f"{self.name} - {self.date}"

    @classmethod
    def get_type(cls, types_list):
        """Helper method to map Nager types to 'national' or 'religious'"""
        if 'Public' in types_list or 'Bank' in types_list:
            return 'national'
        else:
            return 'religious'


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username if self.user else "Anonymous"

from django.utils.text import slugify

class Scrape_MakaziListing(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(unique=True)
    price = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    main_image_url = models.URLField(blank=True, null=True)
    scraped_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_slug_id(self):
        return f"{slugify(self.title)}-{self.id}"


from django.utils.text import slugify

class Scrape_BeforwardListing(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(unique=True)
    price = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    agent_name = models.CharField(max_length=255, blank=True)
    agent_phones = models.JSONField(blank=True, null=True)
    image_urls = models.JSONField(blank=True, null=True)
    scraped_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_slug_id(self):
        return f"{slugify(self.title)}-{self.id}"
