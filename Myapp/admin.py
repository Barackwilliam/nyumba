# admin.py
from .forms import PropertyAdminForm,ClientAdminForm,OfferAdminForm,PartnerAdminForm,PopularPlaceAdminForm,AgentAdminForm,PaymentForm
from django.contrib import admin
from django.utils.safestring import mark_safe

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

# @admin.register(Property)
# class PropertyAdmin(admin.ModelAdmin):
#     list_display = ['title', 'price', 'status', 'region', 'owner', 'is_available']
#     list_filter = ['status', 'region', 'is_available']
#     search_fields = ['title', 'district', 'ward']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    form = PropertyAdminForm
    list_display = ['title', 'price', 'status', 'region', 'owner', 'is_available', 'image_preview']
    list_filter = ['status', 'region', 'is_available']
    search_fields = ['title', 'district', 'ward']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['image_0', 'image_1', 'image_2', 'image_3', 'property_owner_0']:
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'b554dba7565f88537168',  # weka key yako hapa
            })
        return formfield

    def image_preview(self, obj):
        previews = []
        for img_field in ['image_0', 'image_1', 'image_2', 'image_3', 'property_owner_0']:
            img_val = getattr(obj, img_field)
            if img_val:
                previews.append(
                    f'<img src="https://ucarecdn.com/{img_val}/-/format/jpg/-/quality/smart/" '
                    f'style="max-height: 100px; margin-right: 5px;" />'
                )
        return mark_safe("".join(previews)) if previews else "No Image"

    image_preview.short_description = 'Preview'



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
    form = PropertyAdminForm
    list_display = ['user', 'role', 'is_verified', 'subscription_plan']
    list_filter = ['role', 'is_verified']
    search_fields = ['user__username', 'phone']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'profile_picture_1':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'b554dba7565f88537168',  # weka key yako hapa
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'



@admin.register(PopularPlace)
class PopularPlaceAdmin(admin.ModelAdmin):
    form = PopularPlaceAdminForm
    list_display = ['name_of_place', 'number_of_property']
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image_of_place_1':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'b554dba7565f88537168',  # weka key yako hapa
            })
        return formfield

    def image_preview(self, obj):
        if obj.image_of_place_1:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'





@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    form = OfferAdminForm
    list_display = ['title', 'slug']
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'offer_image_1':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'b554dba7565f88537168',  # weka key yako hapa
            })
        return formfield

    def image_preview(self, obj):
        if obj.offer_image_1:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'



# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     form = PaymentForm
#     list_display = ['user', 'timestamp']
    
#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super().formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'Transaction_image_1':
#             formfield.widget.attrs.update({
#                 'role': 'uploadcare-uploader',
#                 'data-public-key': 'b554dba7565f88537168',  # weka key yako hapa
#             })
#         return formfield

#     def image_preview(self, obj):
#         if obj.Transaction_image_1:
#             return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
#         return "No Image"

#     image_preview.short_description = 'Preview'






@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    form = PaymentForm
    list_display = ['user', 'timestamp', 'image_preview']

    def image_preview(self, obj):
        if obj.Transaction_image_1:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height:100px;" />')
        return "No Image"
    image_preview.short_description = 'Preview'

@admin.register(Featured)
class FeaturedAdmin(admin.ModelAdmin):
    list_display = ['f_property_name', 'is_available']



@admin.register(PopularProperty)
class PopularPropertyAdmin(admin.ModelAdmin):
    list_display = ['p_property_name', 'is_available']


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    form = AgentAdminForm
    list_display = ['jina', 'Cheo']
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image_of_agent_1':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'b554dba7565f88537168',  # weka key yako hapa
            })
        return formfield

    def image_preview(self, obj):
        if obj.image_of_agent_1:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'



@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    form = PartnerAdminForm
    list_display = ['jina', 'image_of_partner']
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image_of_partner':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'b554dba7565f88537168',  # weka key yako hapa
            })
        return formfield

    def image_preview(self, obj):
        if obj.image_of_partner:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'

@admin.register(Client)


class ClientAdmin(admin.ModelAdmin):
    form = ClientAdminForm
    list_display = ['name','client_image_1','location','comment']
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'client_image_1':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'b554dba7565f88537168',  # weka key yako hapa
            })
        return formfield

    def image_preview(self, obj):
        if obj.client_image_1:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'


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
