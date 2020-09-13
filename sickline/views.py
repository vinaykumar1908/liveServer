from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sidingz import models as sm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.db.models import Q

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


@login_required
def EMPAD(request):
    qs2 = timezone.now()
    k = sm.ModuleRecieved.objects.all().filter(Q(Wagon1Defect__icontains="em pad") | (Q(Wagon2Defect__icontains="em pad")) | (Q(Wagon3Defect__icontains="em pad"))| (Q(Wagon4Defect__icontains="em pad")) | (Q(Wagon5Defect__icontains="em pad"))).filter(ModuleRecieveDate__month=(qs2.month)).exclude(ModuleDVR=True)

    print(k)
    k = k.order_by('-Date')
    context = {
        'obj': k
    }

    return render(request, 'home/EMPAD.html', context)


@login_required
def Adopter(request):
    qs2 = timezone.now()
    k = sm.ModuleRecieved.objects.all().filter(Q(Wagon1Defect__icontains="adopter") | (Q(Wagon2Defect__icontains="adopter")) | (Q(Wagon3Defect__icontains="adopter"))| (Q(Wagon4Defect__icontains="adopter")) | (Q(Wagon5Defect__icontains="adopter"))).filter(ModuleRecieveDate__month=(qs2.month)).exclude(ModuleDVR=True)

    print(k)
    k = k.order_by('-Date')
    context = {
        'obj': k
    }

    return render(request, 'home/Adopter.html', context)
