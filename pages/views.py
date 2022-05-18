from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageview(TemplateView):
    template_name = 'home.html'

class AboutPageview(TemplateView):
    template_name = 'about.html'