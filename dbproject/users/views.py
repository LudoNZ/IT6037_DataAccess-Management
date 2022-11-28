from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import CustomUser
# Create your views here.
from .forms import CustomUserCreationForm, CustmoUserChangeForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"