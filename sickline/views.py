from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sidingz import models as sm
from django.urls import reverse_lazy
# Create your views here.
class SicklineHomePageView(TemplateView):
    template_name = 'sickline_home.html'


def SicklineModules(request):
    qs = sm.ModuleRecieved.objects.all().filter(ModuleDVS=True)
    print(qs)
    qs = qs.order_by('-Date')
    context = {
        'obj': qs
    }

    return render(request, 'sickline/sicklineModules.html', context)
