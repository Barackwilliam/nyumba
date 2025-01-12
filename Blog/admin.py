from django.contrib import admin
from .models import Contact,BlogPost,Comment
# Register your models here.
admin.site.register(Contact)
admin.site.register(BlogPost)
admin.site.register(Comment)