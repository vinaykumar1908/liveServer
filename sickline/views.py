from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sidingz import models as sm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class SicklineHomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'sickline_home.html'


@login_required
def SicklineModules(request):
    qs = sm.ModuleRecieved.objects.all().filter(ModuleDVS=True).filter(ModuleMadeFit=False)
    print(qs)
    qs = qs.order_by('-Date')
    context = {
        'obj': qs
    }

    return render(request, 'sickline/sicklineModules.html', context)


@login_required
def SicklineModulesFIT(request):
    qs = sm.ModuleRecieved.objects.all().filter(ModuleDVS=True).filter(ModuleMadeFit=True)
    print(qs)
    qs = qs.order_by('-Date')
    context = {
        'obj': qs
    }

    return render(request, 'sickline/sicklineModulesFIT.html', context)
