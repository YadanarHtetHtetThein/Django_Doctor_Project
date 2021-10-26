from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_list, name='doctor-show-list'),
    path('show/all', views.show_doctor, name='doctor-show'),
    path('show/filter/<int:pk>', views.filter_doctor, name='doctor-filter'),
    path('create', views.create_doctor, name='doctor-create'),
    path('category/create', views.create_category, name='doctor-create-category'),
]