from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Person, Property, Listings, Messages, Bids
from .forms import PersonForm, PropertyForm, ListingForm, MessageForm, BidForm

# Person CRUD views
def person_list(request):
    persons = Person.objects.all()
    return render(request, 'home/person_list.html', {'persons': persons})

def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'home/person_form.html', {'form': form})

def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'home/person_form.html', {'form': form})

def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('person_list')

# Property CRUD views
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'home/property_list.html', {'properties': properties})

def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'home/property_form.html', {'form': form})

def property_update(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'home/property_form.html', {'form': form})

def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    property.delete()
    return redirect('property_list')

# Listings, Messages, and Bids CRUD views can be added similarly
