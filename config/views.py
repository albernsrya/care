import logging

from django.shortcuts import render
from django.views.generic import TemplateView


def home_view(request):
    return render(request, "pages/home.html")
