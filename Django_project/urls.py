
from django.contrib import admin
from django.urls import path, include
from  django.conf import settings


from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', loading_page, name='loading'),
    path('', include('Myapp.urls')),
    path('chat/', include('chat.urls')),
    path('Blog/', include('Blog.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    
]



from django.conf.urls import handler404
from Myapp.views import custom_404

handler404 = 'Myapp.views.custom_404'

#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.STATIC_ROOT)
# else:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.STATIC_ROOT)





    
    