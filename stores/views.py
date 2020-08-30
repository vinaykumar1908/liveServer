from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy
from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
from django.http import JsonResponse
import json
import math
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class StoresHomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'stores_home.html'


class RegisterView(LoginRequiredMixin, TemplateView):
     
    template_name = 'stores/Registers.html'


# Views for Current Stock Register start
#class registerCurrentStockListView(ListView):
#    model = models.registerCurrentStock
#   template_name = 'stores/registerCurrentStock/registerCurrentStock.html'
#    ordering = ['-id']
#    paginate_by = 10

class registerCurrentStockCreateView(LoginRequiredMixin, CreateView):
    model =  models.registerCurrentStock
    template_name = 'stores/registerCurrentStock/registerCurrentStock_new.html' 
    fields = '__all__'

class registerCurrentStockDetailView(LoginRequiredMixin, DetailView): 
    model = models.registerCurrentStock 
    template_name = 'stores/registerCurrentStock/registerCurrentStock_detail.html'

class registerCurrentStockEditView(LoginRequiredMixin, UpdateView): 
    model = models.registerCurrentStock
    fields = '__all__' 
    template_name = 'stores/registerCurrentStock/registerCurrentStock_edit.html'


class registerCurrentStockDeleteView(LoginRequiredMixin, DeleteView):
    model = models.registerCurrentStock 
    template_name = 'stores/registerCurrentStock/registerCurrentStock_delete.html' 
    success_url = reverse_lazy('CSR')
# Views for Wheel Recieved from Judw Register end

# Views for Wheel Dispatched from Judw Register start
class registerStockRecievedListView(LoginRequiredMixin, ListView):
    model = models.registerStockRecieved
    template_name = 'stores/registerStockRecieved/registerStockRecieved.html'
    ordering = ['-updateTime']
    paginate_by = 10
    

class registerStockRecievedCreateView(LoginRequiredMixin, CreateView):
    model =  models.registerStockRecieved
    template_name = 'stores/registerStockRecieved/registerStockRecieved_new.html' 
    fields = '__all__'

class registerStockRecievedDetailView(LoginRequiredMixin, DetailView): 
    model = models.registerStockRecieved 
    template_name = 'stores/registerStockRecieved/registerStockRecieved_detail.html'

class registerStockRecievedEditView(LoginRequiredMixin, UpdateView): 
    model = models.registerStockRecieved
    fields = [''] 
    template_name = 'stores/registerStockRecieved/registerStockRecieved_edit.html'

class registerStockRecievedDeleteView(LoginRequiredMixin, DeleteView): 
    model = models.registerStockRecieved 
    template_name = 'stores/registerStockRecieved/registerStockRecieved_delete.html' 
    success_url = reverse_lazy('SRR')
# Views for Wheel Dispatched from Judw Register end


class registerStockDispatchedROH(LoginRequiredMixin, ListView):
    model = models.registerStockDispatchedROH
    template_name = 'stores/registerStockDispatchedROH.html'
    ordering = ['-updateTime']
    paginate_by = 10


class registerStockDispatchSickline(LoginRequiredMixin, ListView):
    model = models.registerStockDispatchedSickline
    template_name = 'stores/registerStockDispatchedSickline.html'
    ordering = ['-updateTime']
    paginate_by = 10


class registerStockDispatchedYard(LoginRequiredMixin, ListView):
    model = models.registerStockDispatchedYard
    template_name = 'stores/registerStockDispatchYard.html'
    ordering = ['-updateTime']
    paginate_by = 10


class registerStockDispatchedTrainDuty(LoginRequiredMixin, ListView):
    model = models.registerStockDispatchedTrainDuty
    template_name = 'stores/registerStockDispatchTrainDuty.html'
    ordering = ['-updateTime']
    paginate_by = 10


@login_required
def currentStockListView(request):
    obj = models.registerCurrentStock.objects.all().order_by('Stock')
    print(obj)
    newObj = obj 
    print("*****newObj****")
    print(newObj)
    for aac in newObj:
        aac.MAC = math.floor((aac.AAC)/12)
        print(aac.MAC)
        print(aac.AAC)
    print("-----newObj-----")
    print(newObj)
    print("-----newObj.MAC-----")
    print(newObj.first().MAC)
    form1 = registerStockRecievedForm()
    form2 = registerStockDispatchROHform()
    form3 = registerStockDispatchSicklineform()
    form4 = registerStockDispatchedYardform()
    form5 = registerStockDispatchedTrainDutyform()
    context = {
        'obj': newObj,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    
    return render(request, 'stores/registerCurrentStock/registerCurrentStock.html', context)


@login_required
def addNewStock(request):
    if request.method == 'POST':
        print(request.POST)
        form = registerStockRecievedForm(request.POST)
        if form.is_valid():
            itemName = request.POST.get('Item')
            stockRecieved = form.cleaned_data['stockRecieved']
            stockRecievedChoices = form.cleaned_data['stockRecievedChoices']
            print("itemName")
            print(itemName)
            print(stockRecieved)
            print(stockRecievedChoices)
        cur = models.registerCurrentStock.objects.get(Item=itemName)
        print(cur)
        curPLNumber = int(cur.PL_Number)
        print(curPLNumber)
        cur.Stock = int(cur.Stock) + int(stockRecieved)
        cur.updateTime = timezone.now()
        print(cur.updateTime)
        cur.save()
        added = models.registerStockRecieved(
            Item=itemName, pl_Number=curPLNumber, stockRecieved=stockRecieved, stockRecievedChoices=stockRecievedChoices,)
        print(added.Item)
        print(added.pl_Number)
        print(added.stockRecieved)
        print(added.stockRecievedChoices)
        added.save()

    obj = models.registerCurrentStock.objects.all().order_by('Stock')

    class newObj(obj):
        def __init__(self, Item, PL_Number, AAC, Stock, updateTime, MAC):
            self.MAC = MAC

    print(obj)
    newObj = obj
    print("*****newObj****")
    print(newObj)
    for aac in newObj:
        aac.MAC = math.floor((aac.AAC)/12)
        print(aac.MAC)
        print(aac.AAC)
    print("-----newObj-----")
    print(newObj)
    print("-----newObj.MAC-----")
    print(newObj.first().MAC)
    form1 = registerStockRecievedForm()
    form2 = registerStockDispatchROHform()
    form3 = registerStockDispatchSicklineform()
    form4 = registerStockDispatchedYardform()
    form5 = registerStockDispatchedTrainDutyform()
    context = {
        'obj': newObj,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    return render(request, 'stores/registerCurrentStock/registerCurrentStock.html', context)


@login_required
def dispatchROH(request):
    if request.method=='POST':
        form = registerStockDispatchROHform(request.POST)
        if form.is_valid():
            itemName = request.POST.get('Item')
            stockDispatchedROH = form.cleaned_data['stockDispatched']
            print(itemName)
            print(stockDispatchedROH)
        cur = models.registerCurrentStock.objects.get(Item=itemName)
        curPLNumber = int(cur.PL_Number)
        print(curPLNumber)
        cur.Stock = int(cur.Stock) - int(stockDispatchedROH)
        cur.updateTime = timezone.now()
        print(cur.updateTime) 
        cur.save()
        added = models.registerStockDispatchedROH(Item=itemName, PL_Number=curPLNumber, stockDispatched=stockDispatchedROH)
        print(added.Item)
        print(added.PL_Number)
        print(added.stockDispatched)
        added.save()
    obj = models.registerCurrentStock.objects.all().order_by('Stock')

    class newObj(obj):
        def __init__(self, Item, PL_Number, AAC, Stock, updateTime, MAC):
            self.MAC = MAC

    print(obj)
    newObj = obj
    print("*****newObj****")
    print(newObj)
    for aac in newObj:
        aac.MAC = math.floor((aac.AAC)/12)
        print(aac.MAC)
        print(aac.AAC)
    print("-----newObj-----")
    print(newObj)
    print("-----newObj.MAC-----")
    print(newObj.first().MAC)
    form1 = registerStockRecievedForm()
    form2 = registerStockDispatchROHform()
    form3 = registerStockDispatchSicklineform()
    form4 = registerStockDispatchedYardform()
    form5 = registerStockDispatchedTrainDutyform()
    context = {
        'obj': newObj,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    return render(request, 'stores/registerCurrentStock/registerCurrentStock.html', context)


@login_required
def dispatchSickline(request):
    if request.method=='POST':
        form = registerStockDispatchSicklineform(request.POST)
        if form.is_valid():
            itemName = request.POST.get('Item')
            stockDispatchedSickline = form.cleaned_data['stockDispatched']
            print(itemName)
            print(stockDispatchedSickline)
        cur = models.registerCurrentStock.objects.get(Item=itemName)
        curPLNumber = int(cur.PL_Number)
        print(curPLNumber)
        cur.Stock = int(cur.Stock) - int(stockDispatchedSickline)
        cur.updateTime = timezone.now()
        print(cur.updateTime) 
        cur.save()
        added = models.registerStockDispatchedSickline(Item=itemName, PL_Number=curPLNumber, stockDispatched=stockDispatchedSickline)
        print(added.Item)
        print(added.PL_Number)
        print(added.stockDispatched)
        print(added.updateTime)
        added.save()
    obj = models.registerCurrentStock.objects.all().order_by('Stock')

    class newObj(obj):
        def __init__(self, Item, PL_Number, AAC, Stock, updateTime, MAC):
            self.MAC = MAC

    print(obj)
    newObj = obj
    print("*****newObj****")
    print(newObj)
    for aac in newObj:
        aac.MAC = math.floor((aac.AAC)/12)
        print(aac.MAC)
        print(aac.AAC)
    print("-----newObj-----")
    print(newObj)
    print("-----newObj.MAC-----")
    print(newObj.first().MAC)
    form1 = registerStockRecievedForm()
    form2 = registerStockDispatchROHform()
    form3 = registerStockDispatchSicklineform()
    form4 = registerStockDispatchedYardform()
    form5 = registerStockDispatchedTrainDutyform()
    context = {
        'obj': newObj,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    return render(request, 'stores/registerCurrentStock/registerCurrentStock.html', context)



@login_required
def dispatchYard(request):
    if request.method=='POST':
        form = registerStockDispatchedYardform(request.POST)
        if form.is_valid():
            itemName = request.POST.get('Item')
            stockDispatchedYard = form.cleaned_data['stockDispatched']
            Yard = form.cleaned_data['Yard']
            print(itemName)
            print(stockDispatchedYard)
            print(Yard)
        cur = models.registerCurrentStock.objects.get(Item=itemName)
        curPLNumber = int(cur.PL_Number)
        print(curPLNumber)
        cur.Stock = int(cur.Stock) - int(stockDispatchedYard)
        cur.updateTime = timezone.now()
        print(cur.updateTime) 
        cur.save()
        added = models.registerStockDispatchedYard(Item=itemName, PL_Number=curPLNumber, stockDispatched=stockDispatchedYard, Yard = Yard)
        print(added.Item)
        print(added.PL_Number)
        print(added.stockDispatched)
        print(added.updateTime)
        print(added.Yard)
        added.save()
    obj = models.registerCurrentStock.objects.all().order_by('Stock')

    class newObj(obj):
        def __init__(self, Item, PL_Number, AAC, Stock, updateTime, MAC):
            self.MAC = MAC

    print(obj)
    newObj = obj
    print("*****newObj****")
    print(newObj)
    for aac in newObj:
        aac.MAC = math.floor((aac.AAC)/12)
        print(aac.MAC)
        print(aac.AAC)
    print("-----newObj-----")
    print(newObj)
    print("-----newObj.MAC-----")
    print(newObj.first().MAC)
    form1 = registerStockRecievedForm()
    form2 = registerStockDispatchROHform()
    form3 = registerStockDispatchSicklineform()
    form4 = registerStockDispatchedYardform()
    form5 = registerStockDispatchedTrainDutyform()
    context = {
        'obj': newObj,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    return render(request, 'stores/registerCurrentStock/registerCurrentStock.html', context)


@login_required
def dispatchTrainDuty(request):
    if request.method=='POST':
        form = registerStockDispatchedTrainDutyform(request.POST)
        if form.is_valid():
            itemName = request.POST.get('Item')
            stockDispatchedTrainDuty = form.cleaned_data['stockDispatched']
#            Yard = form.cleaned_data['Yard']
            print(itemName)
            print(stockDispatchedTrainDuty)
#            print(Yard)
        cur = models.registerCurrentStock.objects.get(Item=itemName)
        curPLNumber = int(cur.PL_Number)
        print(curPLNumber)
        cur.Stock = int(cur.Stock) - int(stockDispatchedTrainDuty)
        cur.updateTime = timezone.now()
        print(cur.updateTime) 
        cur.save()
        added = models.registerStockDispatchedTrainDuty(Item=itemName, PL_Number=curPLNumber, stockDispatched=stockDispatchedTrainDuty)
        print(added.Item)
        print(added.PL_Number)
        print(added.stockDispatched)
        print(added.updateTime)
        added.save()
    obj = models.registerCurrentStock.objects.all().order_by('Stock')

    class newObj(obj):
        def __init__(self, Item, PL_Number, AAC, Stock, updateTime, MAC):
            self.MAC = MAC

    print(obj)
    newObj = obj
    print("*****newObj****")
    print(newObj)
    for aac in newObj:
        aac.MAC = math.floor((aac.AAC)/12)
        print(aac.MAC)
        print(aac.AAC)
    print("-----newObj-----")
    print(newObj)
    print("-----newObj.MAC-----")
    print(newObj.first().MAC)
    form1 = registerStockRecievedForm()
    form2 = registerStockDispatchROHform()
    form3 = registerStockDispatchSicklineform()
    form4 = registerStockDispatchedYardform()
    form5 = registerStockDispatchedTrainDutyform()
    context = {
        'obj': newObj,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    return render(request, 'stores/registerCurrentStock/registerCurrentStock.html', context)


@login_required
def autocomplete(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = models.registerCurrentStock.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(PL_Number__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.Item
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)
            
            return render(request, 'stores/registerCurrentStock/registerCurrentStock.html')


@login_required
def ItemQuickLink(request):
    if request.method == 'POST':
        ItemName = request.POST.get('ItemName')
        print("ItemName")
        print(ItemName)
    qs = models.registerCurrentStock.objects.all().filter(Item=ItemName)
    class newObj(qs):
        def __init__(self, Item, PL_Number, AAC, Stock, updateTime, MAC):
            self.MAC = MAC
    newObj = qs
    print("*****newObj****")
    print(newObj)
    for aac in newObj:
        aac.MAC = math.floor((aac.AAC)/12)
        print(aac.MAC)
        print(aac.AAC)
    #print(newObj.first().MAC)
    form1 = registerStockRecievedForm()
    form2 = registerStockDispatchROHform()
    form3 = registerStockDispatchSicklineform()
    form4 = registerStockDispatchedYardform()
    form5 = registerStockDispatchedTrainDutyform()
    context = {
        'obj': newObj,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
        }
    return render(request, 'stores/registerCurrentStock/registerCurrentStock.html', context)


@login_required
def ItemNameAutocomplete(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = models.registerCurrentStock.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Item__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.Item
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'stores/registerCurrentStock/registerCurrentStock.html')
