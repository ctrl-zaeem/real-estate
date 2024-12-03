from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Person, Property, Listings, Messages, Bids
from .forms import PersonForm, PropertyForm, ListingForm, MessageForm, BidForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, SignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def home(request):
    properties = Property.objects.all()
    return render(request, 'home/index.html', {'properties': properties})

# Person CRUD views
def person_list(request):
    # Check if the user is logged in via session
    if 'person_id' not in request.session:
        messages.error(request, "Please log in to access this page.")
        return redirect('login')

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

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if the username exists
            person = Person.objects.get(name=username)

            # If the password matches, log in the user
            if person.password == password:  # Comparing plain-text passwords for now
                request.session['person_id'] = person.user_id  # Store user_id in session
                messages.success(request, f"Welcome, {person.name}!")
                return redirect('dashboard')  # Redirect to person_list on successful login
            else:
                # If the password is incorrect, show an error message
                messages.error(request, "Invalid password.")
        
        except Person.DoesNotExist:
            # If the username doesn't exist, show an error message
            messages.error(request, "Invalid username or password.")

    return render(request, 'home/login.html')

# Signup View
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Ensure no duplicate users
        if Person.objects.filter(name=name).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return redirect('signup')

        # Create a new Person entry
        Person.objects.create(name=name, email=email, password=password)
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'home/signup.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

# Logout View
@login_required
def logout_view(request):
    request.session.flush()  # Clear the session
    messages.info(request, "You have been logged out.")
    return redirect('login')

# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')

def dashboard_view(request):
    if not request.session.get('person_id'):
        return redirect('login')  # Redirect to login if not logged in
    return render(request, 'home/dashboard.html')

# Bids view (Placeholder)
def bids_view(request):
    return render(request, 'home/bids.html')

# Messages view (Placeholder)
def messages_view(request):
    return render(request, 'home/messages.html')

