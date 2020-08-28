from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class YardHomePageView(TemplateView):
    template_name = 'yard_home.html'

