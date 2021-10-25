from django.shortcuts import render

def home(request):
    context = {
        'title':'Hospital Management System'
    }
    return render(request, 'page/home.html', context)

def about(request):
    context = {
        'title':'About'
    }
    return render(request, 'page/about.html', context)
