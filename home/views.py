from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from stores import models as SM
from sidingz import models as ZM
from django.urls import reverse_lazy
from django.db import models
import math
from home import models as HM
from itertools import filterfalse
#from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
# Create your views here.
from django.contrib.auth.decorators import login_required


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
    
    
    context = {
        'obj': qs1,
        #'obj2': qs2,
    }
    return render(request, 'home.html', context)




