from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctor_Category, Doctor
from .forms import CategoryCreationForm, DoctorCreationForm

def show_list(request):
    categories = Doctor_Category.objects.all()
    context = {
        'title':'Doctor Category List',
        'categories': categories
    }
    return render(request,'doctor/doctor_list.html', context)

def create_category(request):
    if request.method == 'POST':
        form = CategoryCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Created!')
            return redirect('doctor-create-category')
    else:
        form = CategoryCreationForm()
        categories = Doctor_Category.objects.all()
    context = {
        'title':'Doctor Category List',
        'form':form,
        'categories' : categories
    }
    return render(request,'doctor/doctor_cateogory_create.html', context)

def create_doctor(request):
    if request.method == 'POST':
        form = DoctorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor Created!')
            return redirect('doctor-show')
    else:
        form = DoctorCreationForm()
        doctors = Doctor.objects.all()
    context = {
        'title':'Doctor Creation Form',
        'form':form,
        'doctors' : doctors
    }
    return render(request,'doctor/doctor_create.html', context)

def show_doctor(request):
    doctors = Doctor.objects.all()
    context = {
        'title':'Doctor Category List',
        'doctors': doctors
    }
    return render(request,'doctor/doctor_show.html', context)
    
def filter_doctor(request, pk):
    doctors = Doctor.objects.filter(category=pk)
    context = {
        'title':'Filter Doctor',
        'doctors': doctors,
        'category': Doctor_Category.objects.get(pk=pk)
    }
    return render(request,'doctor/doctor_filter.html', context)