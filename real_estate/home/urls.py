from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.person_list, name='person_list'),
    path('person/create/', views.person_create, name='person_create'),
    path('person/edit/<int:pk>/', views.person_update, name='person_update'),
    path('person/delete/<int:pk>/', views.person_delete, name='person_delete'),
    
    path('properties/', views.property_list, name='property_list'),
    path('property/create/', views.property_create, name='property_create'),
    path('property/edit/<int:pk>/', views.property_update, name='property_update'),
    path('property/delete/<int:pk>/', views.property_delete, name='property_delete'),

    # Add URLs for Listings, Messages, and Bids here
]
