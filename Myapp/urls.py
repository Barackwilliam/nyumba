from django.urls import path 
from .views import referral_dashboard,register_view,login_view, offer_list, offer_detail

from . import views 

urlpatterns = [
    path('', views.popular_featured, name='popular_featured'),
    path('chat', views.chat, name='chat'),
    path('final/', views.final, name='final'),
    path('Thanks/', views.Thanks, name='Thanks'),
    path('construction/', views.construction, name='construction'),
    path('jihudumie/', views.jihudumie, name='jihudumie'),
    path('complete/', views.complete, name='complete'),
    #path('toggle_bookmark/<int:property_id>/', views.toggle_bookmark, name='toggle_bookmark'),
    path('Register/', views.Register, name='Register'),
    path('submit_inquiry/<int:property_id>/', views.submit_inquiry, name='submit_inquiry'),
    path('delete_inquiry/<int:id>/', views.delete_inquiry, name='delete_inquiry'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reset_password/', views.reset_password, name='reset_password'),  
    path('login/', views.login, name='login'),
    path('Invoice/', views.Invoice, name='Invoice'),
    path('logout/', views.logout, name='logout'),

    path('referral-dashboard/', referral_dashboard, name='referral_dashboard'),
    path('signup/', register_view, name='register_view'),
    path('login_view/', login_view, name='login_view'),

    path('Get_referral_link/', views.Get_referral_link, name='Get_referral_link'),
    path('invite_friend/', views.invite_friend, name='invite_friend'),

    # path('notifications/', views.notifications_view, name='notifications_view'),
    # path('notifications/mark_as_read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('property_list/', views.property_list, name='property_list'),

    path('offers/', views.offer_list, name='offer_list'),
    path('offers/<slug:slug>/', views.offer_detail, name='offer_detail'),


    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('add_property/', views.add_property, name='add_property'),
    path('search_property/', views.search_property, name='search_property'),
]

