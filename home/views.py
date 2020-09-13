from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from stores import models as SM
from sidingz import models as ZM
from django.urls import reverse_lazy
from django.db import models
import math
from datetime import date, datetime
from home import models as HM
from itertools import filterfalse
#from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required
class HomePageView(TemplateView):
    template_name = 'home.html'


class SuccessPageView(TemplateView):
    template_name = 'success.html'


@login_required
def homeView(request):
    qs = SM.registerCurrentStock.objects.all()


    HM.p.objects.all().delete()
    qs1 = HM.p.objects.all()
    for l in qs:
        
        x = SM.registerCurrentStock.objects.get(id=l.id)
        
        y = HM.p.objects.create(id=x.id, Item=x.Item, AAC=x.AAC, Stock=x.Stock, updateTime=x.updateTime, PL_Number=x.PL_Number)
        y.MACfun()
        y.criticalFun()
        y.save()
        

    qs1 = HM.p.filterCriticalFun(request)
    qs1 = qs1.order_by('Stock')
    rs = ZM.ModuleRecieved.objects.filter(Q(ModulePresentPosition__iendswith="TKD_Sickline") & Q(ModuleDVS=True) & Q(ModuleMadeFit=False))
    rs1 = ZM.ModuleRecieved.objects.filter(Q(ModulePresentPosition__iendswith="TKD_ROH1") & Q(ModuleDVR=True) & Q(ModuleMadeFit=False))
    ROH2 = ZM.ModuleRecieved.objects.filter(Q(ModulePresentPosition__iendswith="TKD_ROH2") & Q(ModuleDVR=True) & Q(ModuleMadeFit=False))
    print('rs')
    print(rs)
    print('rs1')
    print(rs1)
    print('rs2')
    print(ROH2)
    qs2 = timezone.now()
    a = ZM.ModuleRecieved.objects.filter(ModuleRecieveDate__month=(qs2.month))
    k = a.filter(Q(Wagon1Defect__icontains="em pad") | (Q(Wagon2Defect__icontains="em pad")) | (Q(Wagon3Defect__icontains="em pad")) | (Q(Wagon4Defect__icontains="em pad")) | (Q(Wagon5Defect__icontains="em pad"))).filter(ModuleRecieveDate__month=(qs2.month))
    l = a.filter(Q(Wagon1Defect__icontains="adopter") | (Q(Wagon2Defect__icontains="adopter")) | (Q(Wagon3Defect__icontains="adopter")) | (Q(Wagon4Defect__icontains="adopter")) | (Q(Wagon5Defect__icontains="adopter"))).filter(ModuleRecieveDate__month=(qs2.month))
    m = a.filter(Q(ModuleMadeFit=True) & Q(ModuleDVR=True))
    n = a.filter(Q(ModuleMadeFit=True) & Q(ModuleDVS=True))
    o = a.filter(Q(ModuleDVR=True) & Q(ModuleRecieveDate__month=(qs2.month)))
    print(k)
    print(l)

    context = {
        'obj': qs1,
        'obj2': rs,
        'obj3': rs1,
        'ROH2': ROH2,
        'obj4': a,
        'obj5': k,
        'obj6': l,
        'obj7': m,
        'obj8': n,
        'time': qs2,


    }
    return render(request, 'home.html', context)
