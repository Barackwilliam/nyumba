from django.urls import path 
from django.conf import settings
from . import views 
from . views import contact_succes, Contact_us, post_list

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('Blog_post', views.Blog_post, name='Blog_post'),
    path('contact_succes/', views.contact_succes, name='contact_succes'),
    path('Contact_us/', views.Contact_us, name='Contact_us'),
]