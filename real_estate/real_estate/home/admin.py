from django.contrib import admin
from .models import Person, Property, Listings, Messages, Bids

admin.site.register(Person)
admin.site.register(Property)
admin.site.register(Listings)
admin.site.register(Messages)
admin.site.register(Bids)
