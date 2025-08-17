from django import forms 

from django.core.exceptions import ValidationError
from .models import Profile, Property, Inquiry, Payment,Client,Offer,Partner,PopularPlace,Agent,Payment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'address', 'phone', 'role', 'bio', 'profile_picture_1']

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',  # Uploadcare widget
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture_1'].widget.attrs.update({
            'role': 'uploadcare-uploader',
            'data-public-key': "b554dba7565f88537168",

        })
        self.fields['profile_picture_1'].empty_label = "Upload Image"



class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            'full_name', 'phone_number', 'email', 'message'
        ]


class CustomerPasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Old Password")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Confirm Password")

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise ValidationError("Password Hazifanani")
        return cleaned_data


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['Transaction_image']




# class MyForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     captcha = ReCaptchaField()


class PropertyAdminForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]



class ClientAdminForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

class OfferAdminForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]


class PartnerAdminForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]


class PopularPlaceAdminForm(forms.ModelForm):
    class Meta:
        model = PopularPlace
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]


class AgentAdminForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['Transaction_image_1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Transaction_image_1'].widget = forms.HiddenInput(attrs={
            'role': 'uploadcare-uploader',
            'data-public-key': "b554dba7565f88537168",
        })
    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]
