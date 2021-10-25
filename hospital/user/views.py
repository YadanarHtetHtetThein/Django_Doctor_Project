from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
from .models import Profile

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f"User registeration success! User name with {name}")
            return redirect('home-page')
        else:
            messages.warning(request, 'Enter username or password')
            return redirect('user-register-page')
    else:
        form = UserCreationForm()
    context = {
        'title':'User Registeration',
        'form': form,
    }
    return render(request, 'user/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, 'Profile Updated!')
            return redirect('user-profile-page')
    else:
        u_form = UserUpdateForm(instance = request.user)
        if request.user.profile.image:
            p_form = ProfileUpdateForm(instance=request.user.profile)
        else:
            p_form = ''
    context = {
        'title':'User Profile Detail',
        'p_form': p_form,
        'u_form': u_form,
    }
    return render(request, 'user/profile.html', context)
