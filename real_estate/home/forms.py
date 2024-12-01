from django import forms
from .models import Person, Property, Listings, Messages, Bids

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
