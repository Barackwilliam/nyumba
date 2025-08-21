

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, InquiryForm
from django.http import JsonResponse
from django.db.models import Q

from .models import Referral

from django.core.files.storage import default_storage
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.template.loader import get_template
from django.contrib.admin.views.decorators import staff_member_required
from xhtml2pdf import pisa
import openpyxl
from .models import VisitorInfo


from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.models import User, auth
from .models import ChatMessage
from .models import Property,Review,Offer
from django.contrib.auth import update_session_auth_hash
from .forms import CustomerPasswordChangeForm, PaymentForm
# from . models import Notification
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from.models import Profile, Featured,PopularPlace, PopularProperty, Inquiry, Agent, Client,Partner,Holiday
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

PROPERTIES_PER_PAGE = 25



@login_required
def referral_dashboard(request):
    referral = Referral.objects.get(referrer=request.user)
    referral_link = f'{request.build_absolute_uri("/signup")}?ref={referral.referral_code}'
    referrals = Referral.objects.filter(referrer=request.user, referred_user__isnull=False)

    context = {
        'referral_link': referral_link,
        'referrals':referrals,
    }
    return render(request, 'core/dashboard.html', context)
    #return render(request, 'core/test_referral_dashboard.html', context)

@login_required
def Get_referral_link(request):
    referral = Referral.objects.get(referrer=request.user)
    referral_link = f'{request.build_absolute_uri("/signup")}?ref={referral.referral_code}'
    referrals = Referral.objects.filter(referrer=request.user, referred_user__isnull=False)

    context = {
        'referral_link': referral_link,
        'referrals':referrals,
    }
    #return render(request, 'core/dashboard.html', context)
    return render(request, 'core/referral_copy_link.html', context)


def register_view(request):
    ref_code = request.GET.get('ref')
    referrer = None

    if ref_code:
        try:
            referrer = Referral.objects.get(referral_code=ref_code).referrer
        except Referral.DoesNotExist:
            pass

    if request.method == 'POST':
        new_user = User.objects.create_user(username=request.POST['username'], email = request.POST['email'],password=request.POST['password'])   
        if referrer:
            Referral.objects.filter(referral_code=ref_code).update(referred_user=new_user)
            referrer.profile.points += 10
            referrer.profile.save()
        return redirect('login_view')
    return render(request,'core/register_view.html')


@login_required(login_url='login')
def add_property(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        description = request.POST['description']
        property_type = request.POST['property_type']
        country = request.POST['country']
        region =request.POST['region']
        district = request.POST['district']
        ward = request.POST['ward']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        house_size = request.POST['house_size']
        nearby = request.POST['nearby']

        image_0=request.POST.get('image_0')
        image_1=request.POST.get('image_1')
        image_2=request.POST.get('image_2')
        image_3=request.POST.get('image_3')
        property_owner_0=request.POST.get('property_owner_0')
        
        status = request.POST['status']
        p_status = request.POST['p_status']
        # video = request.FILES.get('video')
        business_phone = request.POST['business_phone']
        business_email = request.POST['business_email']
        video_link = request.POST['video_link']



        property = Property.objects.create(title=title, price=price,
        description=description, property_type=property_type,business_phone=business_phone,country=country,business_email=business_email,
        region=region,district=district, ward=ward, bedrooms=bedrooms,
        bathrooms=bathrooms, house_size=house_size, nearby=nearby,video_link=video_link, status=status,owner=request.user, image_0=image_0, image_1=image_1, p_status=p_status,image_2=image_2, image_3=image_3,property_owner_0=property_owner_0)
        return redirect('property_list')
    return render(request,'core/add-property.html')


def construction(request):
    return render(request,'core/under-construction.html')

def Invoice(request):
    return render(request,"core/invoice.html")


def jihudumie(request):
    return render(request,'core/jihudumie.html')


def final(request):
    return render(request,'core/final.html')

def complete(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            return redirect('Thanks')
        else:
            print(form.errors)
    else:
        form = PaymentForm()
    return render(request, 'core/complete.html', {'form': form})

    
def Thanks(request):
    return render(request,'core/Thanks.html')







@login_required(login_url='login')
def dashboard(request):
    properties = Property.objects.filter(owner=request.user)
    total_views = sum(property.view_count for property in properties)
    total_published_property = properties.count()
    # total_bookmarked = sum(property.bookmarks.count() for property in properties)
    inquiries = Inquiry.objects.filter(owner=request.user)
    inquiry_count = inquiries.count()


    context = {
        'inquiry_count':inquiry_count,
        'inquiries':inquiries,
        'properties':properties,
        'total_views':total_views,
        'total_published_property':total_published_property,
        # 'total_bookmarked':total_bookmarked,

    }

    return render(request, 'core/user_dashboard.html', context)


# @login_required(login_url='login')
def property_list(request):
    prop_list = Property.objects.all().order_by('-date_posted')

    # **Chukua title za nyumba chache kwa ajili ya SEO**
    property_titles = ", ".join(prop_list.values_list('title', flat=True)[:3])  
    page_title = f"{property_titles} - Nyumba za Kupanga na Kuuza Tanzania" if property_titles else "NyumbaChap - Tafuta Nyumba"

    # **Pagination**
    page = request.GET.get('page', 1)
    property_paginator = Paginator(prop_list, PROPERTIES_PER_PAGE)

    try:
        prop_list = property_paginator.page(page)
    except PageNotAnInteger:
        prop_list = property_paginator.page(1)
    except EmptyPage:
        prop_list = property_paginator.page(property_paginator.num_pages)

    context = {
        "page_obj": prop_list,
        "prop_list": prop_list,
        "is_paginated": property_paginator.num_pages > 1,
        "paginator": property_paginator,
        "page_title": page_title  # **Title ya ukurasa**
    }

    return render(request, 'core/property_list.html', context)


@login_required(login_url='login')
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)  # Fetch property using id and slug
    property.add_view(request.user)  # Increment view count and add viewer
    return render(request, 'core/single_property.html', {'property': property})

@login_required(login_url='login')
def offer_list(request):
    offers = Offer.objects.all()
    return render(request, 'core/offer_list.html', {'offers': offers})
@login_required(login_url='login')
def offer_detail(request, slug):
    offer = get_object_or_404(Offer, slug=slug)
    return render(request, 'core/offer_detail.html', {'offer': offer})
 
@login_required(login_url='login')
def popular_properties(request):
    popular_p = Property.objects.all()
    context ={
        "popular_p":popular_p,
    }
    return render(request,'core/home1.html',context)



# @login_required(login_url='login')
def search_property(request):
    query = request.GET.get('q') #Fetching the user's input from the search box

    results = Property.objects.all()

    if query:
         results = results.filter(Q(region__icontains=query) |
        Q(district__icontains=query) |
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(status__icontains=query) |
        Q(bedrooms__iexact=query) |
        Q(ward__icontains=query) |
        Q(price__iexact=query))

    return render(request,'core/searched.html',{'results':results})



import requests
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Profile
# from .utils import send_welcome_email  # ensure this exists

def Register(request):
    if request.method == 'POST':
        try:
            # reCAPTCHA verification
            recaptcha_response = request.POST.get('g-recaptcha-response')
            recaptcha_data = {
                'secret': '6Lfr4xUrAAAAAHJxI7wm4xFza7BTBYotysJocKbn',
                'response': recaptcha_response
            }
            recaptcha_verify = requests.post('https://www.google.com/recaptcha/api/siteverify', data=recaptcha_data)
            result = recaptcha_verify.json()

            if not result.get('success'):
                messages.error(request, 'Tafadhari thibitisha kuwa wewe si robot kwa kutumia reCAPTCHA.')
                return redirect('Register')

            # form data
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            if password != password2:
                messages.error(request, 'Nenosiri halilingani. Tafadhari jaribu tena.')
                return redirect('Register')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email hii tayari imesajiliwa. Tafadhari tumia nyingine.')
                return redirect('Register')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username hii tayari ipo. Tafadhari chagua nyingine.')
                return redirect('Register')

            # create user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # authenticate and login user
            user_login = auth.authenticate(username=username, password=password)
            if user_login is not None:
                auth.login(request, user_login)

            # update profile fields after it's auto-created by signal
            profile = user.profile
            profile.email = email
            profile.role = 'customer'
            profile.save()

            # send welcome email (optional)
            send_welcome_email(user.email, user.username)

            messages.success(request, 'Akaunti yako imeundwa kikamilifu. Karibu Nyumbachap!')
            return redirect('login')

        except requests.exceptions.RequestException:
            messages.error(request, 'Tatizo la mtandao lilitokea wakati wa reCAPTCHA. Tafadhari jaribu tena.')
            return redirect('Register')

        except Exception as e:
            messages.error(request, f"Hitilafu isiyotegemewa imetokea: {str(e)}")
            return redirect('Register')

    return render(request, 'core/Register.html')



@login_required(login_url='login')
def reset_password(request):
    if request.method == 'POST':
        form = CustomerPasswordChangeForm(request.POST)
        if form.is_valid():
            user = request.user 
            #Hakikisha old password ni sahihi
            if not user.check_password(form.cleaned_data['old_password']):
                messages.error(request, 'Password ya Zamani sio Sahihi..!')
            else:
                user.set_password(form.cleaned_data['new_password'])
                user.save()

                update_session_auth_hash(request, user)#keep logged in user after password change
                messages.success(request, 'Password Imebadilishwa..!')
                return redirect('reset_password')
        else:
            form = CustomerPasswordChangeForm()
    return render(request, 'core/change-password.html')

                



@login_required(login_url='login')
def chat(request):
    return render(request, 'core/chat.html')




@login_required(login_url='login')
def submit_inquiry(request,property_id):
    property = get_object_or_404(Property, id=property_id)
    owner = property.owner #Assuming that the property owner has an owner field linked to user

    if request.method=='POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.property=property
            inquiry.owner = owner
            inquiry.user = request.user
            inquiry.save()

        return redirect('property_detail',property_id=property.id)

    else:
        form = InquiryForm()
        return render(request, 'core/single_property.html',{'form':form,'property':property})



@login_required
def delete_inquiry(request,id):
    inquiry = get_object_or_404(Inquiry, id=id, owner=request.user) #ensure only owner can delete
    inquiry.delete()
    return redirect('dashboard')



from .utils import *
from django.utils import timezone



def popular_featured(request):

    featured = Featured.objects.filter(f_property_name__is_available=True)#filter only available featured properties
    popular = PopularPlace.objects.all()
    agents = Agent.objects.all()
    partners = Partner.objects.all()
    clients = Client.objects.all()
    popular_properties = PopularProperty.objects.filter(p_property_name__is_available=True)#filter only available popular properties
    context = {
        'popular_properties':popular_properties,
        "popular":popular,
        'featured': featured,
        'agents':agents,
        'partners':partners,
        'clients':clients,
    }

    ip = get_client_ip(request)
    region = get_region_by_ip(ip)
    user = request.user if request.user.is_authenticated else None

    # Angalia kama visitor tayari yupo kwa ip + user
    visitor, created = VisitorInfo.objects.get_or_create(
        ip_address=ip,
        user=user,
        defaults={'region': region}
    )

    if not created:
        visitor.visit_count += 1

        # Kama hatujaweka region awali au imebadilika, irekebishwe
        if region and (not visitor.region or visitor.region != region):
            visitor.region = region

        visitor.last_visit = timezone.now()
        visitor.save()
    return render(request, 'core/home.html', context)




@login_required(login_url='login')

def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)  # Hii inahakikisha profile ipo
    
    form = None  # Initialize form variable

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')  # Badilisha na URL yako
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'core/profile_settings.html', {'form': form})

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')



import requests  # On top if not already

def login(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': '6Lfr4xUrAAAAAHJxI7wm4xFza7BTBYotysJocKbn',
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            username = request.POST['username']
            password = request.POST['password']
            User = auth.authenticate(username=username, password=password)
            if User is not None:
                auth.login(request, User)
                return redirect('/')
            else:
                messages.error(request, 'Tafadhari ingiza Taarifa Sahihi na Ujaribu Tena au Jisajili Upya!')
                return redirect(login)
        else:
            messages.error(request, 'ReCAPTCHA verification imeshindwa. Tafadhari jaribu tena.')
            return redirect(login)
    else:
        return render(request, 'core/login.html')

    


def login_view(request):
    if request.method =='POST':
       username = request.POST['username']
       password = request.POST['password']
       User = auth.authenticate(username=username, password=password)
       if User is not None: # type: ignore
          auth.login(request, User) # type: ignore
          return redirect('referral_dashboard')
       else:
        messages.error(request, 'Taarifa Sio Sahihi Tafadhari Jaribu Tena!')
        return redirect(login_view)
    else:
        return render(request,'core/login.html')




@login_required(login_url='login')
def referral_copy_link(request):
    return render(request, "core/referral_copy_link.html")


@login_required(login_url='login')
def invite_friend(request):
    return render(request, "core/invite_friend.html")



 ############33#####33###33######33
#######333##3####333####3######333##
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


def send_welcome_email(to_email, user_name):
    subject = "Welcome to NyumbaChap!"
    context = {
        'user_name': user_name,
        'subject': subject,
    }
    message = render_to_string('core/welcome.html', context)  # Load the email template
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        html_message=message,  # Ensures it is sent as an HTML email
    )




def send_custom_email(to_email, user_name, subject, message_content):
    """Function ya kutuma email na ujumbe wa mfumo"""
    context = {
        'user_name': user_name,
        'subject': subject,
        'message_content': message_content
    }
    message = render_to_string('core/email_template.html', context)  
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        html_message=message,
    )

def send_email_to_selected(request):
    users = User.objects.all()  # Chukua watumiaji wote kwenye mfumo

    if request.method == 'POST':
        user_ids = request.POST.getlist('user_ids')  # Chagua watumiaji
        subject = request.POST.get('subject')  # Pata kichwa cha email
        message_content = request.POST.get('message')  # Pata ujumbe wa email

        if not user_ids:
            messages.error(request, "Tafadhali chagua angalau mtumiaji mmoja.")
            return redirect('send_email_selected')

        selected_users = User.objects.filter(id__in=user_ids)
        for user in selected_users:
            send_custom_email(user.email, user.username, subject, message_content)

        messages.success(request, f'Email imetumwa kwa watu {len(selected_users)} !')
        return redirect('send_email_selected')  # Rudi kwenye ukurasa wa send_email.html

    return render(request, 'core/send_email.html', {'users': users})



def send_email_to_all(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message_content = request.POST.get('message')

        users = User.objects.all()
        for user in users:
            send_custom_email(user.email, user.username, subject, message_content)

        messages.success(request, f'Email sent to {users.count()} users successfully!')
        return redirect('send_email_all')  # Hakikisha jina hili lipo kwenye `urls.py`

    return render(request, 'core/send_email_all.html')




from datetime import timedelta
from django.utils.timezone import now
from django.core.management.base import BaseCommand
@login_required(login_url='login')
def remove_expired_verifications():
    """ Hii function itaondoa verification kwa accounts zilizoisha muda """
    expiry_date = now() - timedelta(days=30)
    expired_profiles = Profile.objects.filter(is_verified=True, verified_at__lte=expiry_date)
    
    # Ondoa verification
    for profile in expired_profiles:
        profile.is_verified = False
        profile.verified_at = None  # Reset tarehe
        profile.save()
        print(f"Verification removed for {profile.user.username}")

# Run function kila siku
class Command(BaseCommand):
    help = "Disable expired verifications"

    def handle(self, *args, **kwargs):
        remove_expired_verifications()



from . utils import remove_expired_verifications
@login_required(login_url='login')
def dashboard_view(request):
    remove_expired_verifications()  # Angalia ikiwa verification ime-expire
    return render(request, "core/user_dashboard.html")


def email(request):
    return render(request,'core/email.html')



from django.http import JsonResponse
from .serializers import PropertySerializer

def property_list_view(request):
    region = request.GET.get('region')
    district = request.GET.get('district')
    ward = request.GET.get('ward')

    properties = Property.objects.all()

    if region:
        properties = properties.filter(region=region)
    if district:
        properties = properties.filter(district=district)
    if ward:
        properties = properties.filter(ward=ward)

    serializer = PropertySerializer(properties, many=True)
    return JsonResponse(serializer.data, safe=False)




from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_lat_lon(location_name):
    """
    Use Geopy to get latitude and longitude for the location name.
    """
    geolocator = Nominatim(user_agent="myGeocoder")
    
    try:
        location = geolocator.geocode(location_name)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None  # Location not found
    except GeocoderTimedOut:
        return None, None  # Handle timeout, return None





def property_map(request):
    return render(request, 'core/map.html')



from .models import Property, PropertyLocation

def update_property_locations():
    """
    Loop through all properties, fetch their location name (region, district, ward),
    and update the PropertyLocation with lat and lon using geocoding.
    """
    properties = Property.objects.all()

    for property in properties:
        location_name = f"{property.region}, {property.district}, {property.ward}"
        lat, lon = get_lat_lon(location_name)  # Use geocoding to get lat/lon

        if lat and lon:
            # Check if PropertyLocation already exists
            property_location, created = PropertyLocation.objects.get_or_create(property=property)

            # Update or set lat/lon values
            property_location.lat = lat
            property_location.lon = lon
            property_location.save()  # Save the updated PropertyLocation

            print(f"Updated {property.title} with coordinates: ({lat}, {lon})")
        else:
            print(f"Failed to update coordinates for {property.title} (Location not found)")



def policy(request):
    return render(request,"core/policy.html")




def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)


from django.http import HttpResponse

def my_view(request):
    response = HttpResponse("Hello, Nyumbachap Does not Accept iframe")
    response["X-Frame-Options"] = "DENY"
    return response




from .models import Help_Question
from django.db.models import Q

def help_center(request):
    query = request.GET.get('q', '')  # Pata neno la utafutaji
    questions = Help_Question.objects.all()
    
    if query:
        questions = questions.filter(Q(question__icontains=query) | Q(answer__icontains=query))
        if not questions.exists():
            return render(request, 'core/help_center.html', {
                'questions': questions,
                'query': query,
                'no_results': True  # Tuma flag ya "hakuna matokeo"
            })
    
    return render(request, 'core/help_center.html', {
        'questions': questions,
        'query': query
    })



from datetime import date
from django.urls import reverse
from .models import Holiday

def upcoming_holidays(request):
    today = date.today()
    holidays = Holiday.objects.filter(date__gte=today).order_by('date')

    # Kuangalia kama leo ni sikukuu
    todays_holiday = Holiday.objects.filter(date=today).first()

    marquee_message = None
    if todays_holiday:
        holidays_url = reverse('upcoming_holidays')
        marquee_message = (
            f'Timu ya NyumbaChap inawatakia <strong>{todays_holiday.name}</strong> njema! '
            f'Tuna matumaini mtafurahia siku hii maalum. '
            f'<a href="{holidays_url}" style="color: #00ffd0; text-decoration: underline;">Tazama Sikukuu Zinazofuata</a>'
        )
        

    return render(request, 'core/upcoming.html', {
        'holidays': holidays,
        'marquee_message': marquee_message
    })


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback

def submit_feedback(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        name = request.POST.get('name', '')
        user = request.user if request.user.is_authenticated else None

        if not comment or not rating:
            return JsonResponse({'success': False, 'error': 'Missing fields'})

        Feedback.objects.create(
            user=user,
            name=name if not user else user.username,
            comment=comment,
            rating=int(rating)
        )

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request'})


from django.db.models import Avg, Count
from django.core.paginator import Paginator

def feedback_dashboard(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    stats = Feedback.objects.aggregate(avg_rating=Avg('rating'), total_feedback=Count('id'))
    paginator = Paginator(feedbacks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/feedbacks_dashboard.html', {
        'page_obj': page_obj,
        'stats': stats
    })





    # API endpoint
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Scrape_MakaziListing
from .serializers import ScrapeMakaziListingSerializer

@api_view(['POST'])
def receive_listing(request):
    serializer = ScrapeMakaziListingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Listing saved successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .models import Scrape_BeforwardListing
from .serializers import ScrapeBeforwardListingSerializer

@api_view(['POST'])
def receive_beforward_listing(request):
    serializer = ScrapeBeforwardListingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Listing saved successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# views.py
from django.shortcuts import render, get_object_or_404
from .models import Scrape_MakaziListing,Scrape_BeforwardListing
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.db.models import Q





def makazi_list(request):
    search_query = request.GET.get('search', '')  # Hii inachukua maneno ya kutafuta kutoka kwa GET query string

    # Tafuta nyumba kulingana na title, location, au description
    listings = Scrape_MakaziListing.objects.all().order_by('-scraped_at')

    if search_query:
        listings = listings.filter(
            Q(title__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(listings, 10)  # Kuonyesha nyumba 10 kwa kila ukurasa
    page_number = request.GET.get('page')  # Hii itachukua namba ya ukurasa kutoka kwa query string
    page_obj = paginator.get_page(page_number)
    default_listings = Scrape_MakaziListing.objects.all().order_by('-scraped_at')



    # Tuma data kwa template
    return render(request, 'core/makazi_list.html', {'page_obj': page_obj, 'search_query': search_query,'default_listings': default_listings,
})

def makazi_detail(request, slug_id):
    pk = slug_id.split('-')[-1]  # Extract ID from the slug
    listing = get_object_or_404(Scrape_MakaziListing, pk=pk)
    return render(request, 'core/makazi_detail.html', {'listing': listing})





def Beforward_list(request):
    search_query = request.GET.get('search', '')
    listings = Scrape_BeforwardListing.objects.all().order_by('-scraped_at')

    if search_query:
        listings = listings.filter(
            Q(title__icontains=search_query) |
            Q(city__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    paginator = Paginator(listings, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Chukua makazi ya default (mfano 3 ya hivi karibuni)
    default_listings = Scrape_BeforwardListing.objects.all().order_by('-scraped_at')

    return render(request, 'core/Beforward_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'default_listings': default_listings,
    })
def Beforward_detail(request, slug_id):
    try:
        obj_id = int(slug_id.split('-')[-1])
    except (ValueError, IndexError):
        return render(request, '404.html', status=404)

    listing = get_object_or_404(Scrape_BeforwardListing, id=obj_id)

    return render(request, 'core/Beforward_detail.html', {
        'listing': listing
    })


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json




@csrf_exempt  # Epuka CSRF kwa ajili ya mfano huu 
def save_visitor_info(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ip = data.get('ip')
            region = data.get('region')
            user = request.user if request.user.is_authenticated else None

            # Kuhifadhi taarifa za visitor (bila kubadili logic yako)
            visitor, created = VisitorInfo.objects.get_or_create(
                ip_address=ip,
                user=user,
                defaults={'region': region}
            )

            if not created and region and (not visitor.region or visitor.region != region):
                visitor.region = region
                visitor.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

