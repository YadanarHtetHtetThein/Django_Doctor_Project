from django import forms
from django.db.models import fields
from .models import Doctor_Category, Doctor

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Doctor_Category
        fields = '__all__'

class DoctorCreationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['category', 'name', 'qualifications', 'duty']