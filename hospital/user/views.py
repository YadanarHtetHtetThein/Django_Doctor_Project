from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"User registeration success! name with {request.user.username}")
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
