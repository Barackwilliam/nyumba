from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, InquiryForm
from django.http import JsonResponse
from django.db.models import Q

from .models import Referral

from django.core.files.storage import default_storage


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
from.models import Profile, Featured,PopularPlace, PopularProperty, Inquiry, Agent, Client,Partner
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

PROPERTIES_PER_PAGE = 20



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
        image = request.FILES['image']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']
        status = request.POST['status']
        p_status = request.POST['p_status']
        # video = request.FILES.get('video')
        business_phone = request.POST['business_phone']
        business_email = request.POST['business_email']
        video_link = request.POST['video_link']
        property_owner = request.FILES['property_owner']



        property = Property.objects.create(title=title, price=price,
         description=description, property_type=property_type,business_phone=business_phone,country=country,business_email=business_email,
        region=region,district=district, ward=ward, bedrooms=bedrooms,
        bathrooms=bathrooms, house_size=house_size, nearby=nearby,video_link=video_link, status=status,owner=request.user, image=image, image1=image1, p_status=p_status,image2=image2, image3=image3,property_owner=property_owner)
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
    form = None
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            return redirect('Thanks')
        else:
            form = PaymentForm()
            print(form.errors)
    return render(request,'core/complete.html',{'form':form})

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


@login_required(login_url='login')
def property_list(request):
    prop_list = Property.objects.all().order_by('-date_posted')

    #paginator
    page = request.GET.get('page',1)
    property_paginator = Paginator(prop_list, PROPERTIES_PER_PAGE)


    try:
        prop_list = property_paginator.page(page)
    except PageNotAnInteger:
        prop_list = property_paginator.page(1)

    except EmptyPage:
        pro_list = property_paginator.page(property_paginator.num_pages)
    except:
        prop_list = property_paginator.page(PROPERTIES_PER_PAGE)
    context = {
        "page_obj":prop_list,
       "prop_list":prop_list,
      'is_paginated': True,
      'paginator': property_paginator,
    }


    return render(request,'core/property_list.html',context)


@login_required(login_url='login')
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    property.add_view(request.user) 
    return render(request, 'core/single_property.html',{'property': property,})



def offer_list(request):
    offers = Offer.objects.all()
    return render(request, 'core/offer_list.html', {'offers': offers})

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



@login_required(login_url='login')
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


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
           if User.objects.filter(email=email).exists():
               messages.error(request, 'Pole..! Email hii Tayari imesajiliwa Tafadhari Tumia Email Nyingine.!')
               return redirect('Register')
           elif User.objects.filter(username=username).exists():
               messages.error(request, 'Loh Username uliyotumia ilisha sajiliwa Tafadhari Tumia Username Nyingine.!')
               return redirect('Register')
           else:
               user = User.objects.create_user(username=username, email=email, password=password2)
               user.save()
               messages.success(request,'Your Account created Successfully login below')
               return redirect('login')
            # #redirect usert to setting
               user_login = auth.authenticate(username=username, password=password)
               auth.login(request, user_login)
            #create a profile object for new user
               user_model = User.objects.get(username=username)
               new_profile = Profile.objects.create(user=user_model,role=user_model,address=user_model,phone=user_model,email=user_model,picture=user_model, bio=user_model)
               new_profile.save()
               return redirect('login')
        else:
            messages.error(request, 'password Not Matching')
            return render(request,'core/login.html')
    else:
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
                #Badirisha password na hakikisha mtumiaji anaendelea ku-login

            # elif new_password != confirm_password:               
            #     messages.error(request, "Password Hazifanani")
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





# #@login_required(login_url='login')
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
    return render(request, 'core/home.html', context)




@login_required(login_url='login')
def edit_profile(request):
    profile = request.user.profile
    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('edit_profile') 
        

    else:
        form = ProfileForm(instance=profile)
    return render(request, "core/profile_settings.html", {'form':form})


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')




def login(request):
    if request.method =='POST':
       username = request.POST['username']
       password = request.POST['password']
       User = auth.authenticate(username=username, password=password)
       if User is not None: # type: ignore
          auth.login(request, User) # type: ignore
          return redirect('/')
       else:
        messages.error(request, 'Tafadhari ingiza Taarifa Sahihi na Ujaribu Tena au Jisajili Upya!')
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





def referral_copy_link(request):
    return render(request, "core/referral_copy_link.html")



def invite_friend(request):
    return render(request, "core/invite_friend.html")



