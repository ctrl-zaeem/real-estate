from django import forms
from .models import Person, Property, Listings, Messages, Bids
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'password', 'user_type', 'verification_state']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'address', 'area', 'city', 'condition', 'property_type']

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listings
        fields = ['property', 'user', 'listing_status']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['sender', 'receiver', 'property', 'message']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bids
        fields = ['property', 'user', 'bid_amount']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

