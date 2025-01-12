from django import forms 
from django.core.exceptions import ValidationError
from .models import Profile, Property, Inquiry, Payment

class ProfileForm(forms.ModelForm): 

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'role',
            'address',
            'bio',
            'profile_picture',
            'phone'
        ]

# class PropertyForm(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = '__all__'
#         widgets = {
#             'video':
#             forms.FileInput(attrs={'accept':'video/*'}),
#         }



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