# decorators.py
from django.shortcuts import redirect
from django.contrib import messages

def client_not_logged_in(view_func):
    def wrapper(request, *args, **kwargs):
        if 'client_id' in request.session:
            messages.warning(request, 'Vous êtes déjà connecté en tant que client.')
            return redirect('client_home')
        return view_func(request, *args, **kwargs)
    return wrapper

def boutique_not_logged_in(view_func):
    def wrapper(request, *args, **kwargs):
        if 'boutique_id' in request.session:
            messages.warning(request, 'Vous êtes déjà connecté en tant que boutique.')
            return redirect('boutique_home')
        return view_func(request, *args, **kwargs)
    return wrapper

def client_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'client_id' not in request.session:
            messages.error(request, 'Veuillez vous connecter en tant que client.')
            return redirect('client_login')
        return view_func(request, *args, **kwargs)
    return wrapper