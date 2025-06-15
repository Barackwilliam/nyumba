from django.urls import path 
from .views import save_visitor_info

from .views import referral_dashboard,register_view,login_view, offer_list, offer_detail
from .views import property_map
from .views import receive_listing, receive_beforward_listing #API urls


from . import views 

urlpatterns = [
    path('save-visitor-info/', save_visitor_info, name='save_visitor_info'),
    path('', views.popular_featured, name='popular_featured'),
    # path('', views.loading_page, name='loading'),
    path('upcoming_holidays', views.upcoming_holidays, name='upcoming_holidays'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedbacks/', views.feedback_dashboard, name='feedback_dashboard'),


    # Scrapped details
    path('api/receive-listing/', receive_listing, name='receive_listing'),# API url
    path('api/receive-beforward-listing/', receive_beforward_listing, name='receive_beforward_listing'),# API url
    path('makazi/', views.makazi_list, name='makazi_list'),
    path('makazi/<slug:slug_id>/', views.makazi_detail, name='makazi_detail'),
    path('Beforward/', views.Beforward_list, name='Beforward_list'),
    path('Beforward/<slug:slug_id>/', views.Beforward_detail, name='Beforward_detail'),






    path('chat', views.chat, name='chat'),
    path('final/', views.final, name='final'),
    path('Thanks/', views.Thanks, name='Thanks'),
    path('construction/', views.construction, name='construction'),
    path('jihudumie/', views.jihudumie, name='jihudumie'),
    path('complete/', views.complete, name='complete'),
    #path('toggle_bookmark/<int:property_id>/', views.toggle_bookmark, name='toggle_bookmark'),  
    path('Register/', views.Register, name='Register'),
    path('send-email-selected/', views.send_email_to_selected, name='send_email_selected'),
    path('send-email-all/', views.send_email_to_all, name='send_email_all'),
    path('email/', views.email, name='email'),

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
    #path('property/<int:property_id>/<slug:slug>/', views.property_detail, name='property_detail'),  # URL for property details with id and slug



    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('add_property/', views.add_property, name='add_property'),
    path('search_property/', views.search_property, name='search_property'),
    path('policy/', views.policy, name='policy'),
    path('help/', views.help_center, name='help_center'),



    path('map/', property_map, name='property_map'),
    path('api/properties/', views.property_list_view, name='property_list_api'),  # API endpoint for property data





]


