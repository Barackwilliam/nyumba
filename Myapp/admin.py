# admin.py
from django.contrib import admin
from .models import (
    Referral, Property, ChatMessage, Review, Profile,
    PopularPlace, Offer, Payment, Featured,
    PopularProperty, Agent, Partner, Client, Inquiry,
    PropertyLocation,
    Help_Question,
    Holiday,
    Feedback,
    Scrape_MakaziListing,Scrape_BeforwardListing
)

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ['referrer', 'referred_user', 'referral_code', 'status', 'rewarded', 'created_at']
    search_fields = ['referral_code', 'referrer__username']

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status', 'region', 'owner', 'is_available']
    list_filter = ['status', 'region', 'is_available']
    search_fields = ['title', 'district', 'ward']

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'timestamp']
    search_fields = ['sender__username', 'receiver__username']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating']
    search_fields = ['user__username']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'is_verified', 'subscription_plan']
    list_filter = ['role', 'is_verified']
    search_fields = ['user__username', 'phone']

@admin.register(PopularPlace)
class PopularPlaceAdmin(admin.ModelAdmin):
    list_display = ['name_of_place', 'number_of_property']

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp']

@admin.register(Featured)
class FeaturedAdmin(admin.ModelAdmin):
    list_display = ['f_property_name', 'is_available']

@admin.register(PopularProperty)
class PopularPropertyAdmin(admin.ModelAdmin):
    list_display = ['p_property_name', 'is_available']

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['jina', 'Cheo']

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['jina', 'image_of_partners']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','client_image','location','comment']


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'email', 'property', 'owner', 'date_sent']
    search_fields = ['full_name', 'phone_number', 'email', 'property__title']

@admin.register(PropertyLocation)
class PropertyLocationAdmin(admin.ModelAdmin):
    list_display = ['property', 'lat', 'lon']
    search_fields = ['property__title']

@admin.register(Help_Question)
class HelpQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_at']
    search_fields = ['question']

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'type', 'country']
    list_filter = ['type', 'country']
    search_fields = ['name']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'rating', 'created_at']
    search_fields = ['name', 'user__username']

# Scraped_MakaziListing
class ScrapeMakaziListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'scraped_at')
    search_fields = ('title', 'location')
    list_filter = ('scraped_at',)
admin.site.register(Scrape_MakaziListing, ScrapeMakaziListingAdmin)




class ScrapeBeforwardListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'link','price', 'city','agent_name','agent_phones','image_urls', 'scraped_at')
    search_fields = ('title', 'city','price','agent_name','agent_phones')
    list_filter = ('scraped_at',)
admin.site.register(Scrape_BeforwardListing, ScrapeBeforwardListingAdmin)


# admin.py
from django.contrib import admin
from .models import VisitorInfo

@admin.register(VisitorInfo)
class VisitorInfoAdmin(admin.ModelAdmin):
    list_display = ('user','ip_address', 'region', 'visit_count', 'first_visit', 'last_visit')
    list_filter = ('user','region',)
    search_fields = ('user','ip_address',)
