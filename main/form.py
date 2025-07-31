from django import forms
from .models import form
from rest_framework import serializers


class FormModelForm(forms.ModelForm):
    class Meta:
        model = form
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = form
        fields = '__all__'