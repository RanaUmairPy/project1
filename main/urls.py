from django.contrib import admin
from django.urls import path
from main.views import index,delete,form_api,delete_form,update_form
urlpatterns = [
   path('', index),
   path('delete/', delete, name='delete'),
   path('api/', form_api, name='form_api'),
   path('delete_form/<int:pk>/', delete_form, name='delete_form'),
   path('update_form/<int:pk>/', update_form, name='update_form'),
]
