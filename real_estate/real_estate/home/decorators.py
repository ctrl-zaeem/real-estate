from django.shortcuts import redirect

def login_required(function):
    def wrap(request, *args, **kwargs):
        if 'person_id' not in request.session:
            return redirect('login')  # Redirect to your custom login page
        return function(request, *args, **kwargs)
    return wrap
