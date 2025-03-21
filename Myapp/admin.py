from django.contrib import admin
from .models import Profile
from .models import Property
from .models import Featured
from .models import Inquiry, Agent,Client,Partner, Offer,Payment
from .models import PopularPlace, PopularProperty,ChatMessage,Referral,PropertyLocation
# from . models import Notification
# from chat.models import ChatRoom
# from chat.models import Message

# Register your models here.

# admin.site.register(ChatRoom)

# admin.site.register(Message)
admin.site.register(Referral)
admin.site.register(PropertyLocation)
admin.site.register(Offer)
admin.site.register(Partner)
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(Inquiry)
# admin.site.register( Notification)
admin.site.register(ChatMessage)
admin.site.register(Featured)
admin.site.register(Profile)
admin.site.register(Property)
admin.site.register(Payment)
admin.site.register(PopularPlace)
admin.site.register(PopularProperty)


# @admin.register(Property)
# class PropertyAdmin(admin.ModelAdmin):
#     list_display = ('unique_id')