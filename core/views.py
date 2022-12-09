from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView

class BirbaloView(TemplateView):
    template_name = 'birbalo.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
