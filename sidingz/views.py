from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sidingz import models
from django.urls import reverse_lazy
# from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.


class SidingHomePageView(TemplateView):
    template_name = 'sidings_home.html'


class SidingICDOkhlaHomePageView(TemplateView):
    template_name = 'sidings/ICD_Okhla_home.html'


class SidingModuleRecievedPageView(CreateView):
    model = models.ModuleRecieved
    template_name = 'sidings/ModuleRecieved.html'
    fields = ['RakeNumber', 'BPC_Number',
              'ModulePresentPosition',
              'LineNumber', 'ModuleName',
              'ModuleROHDate', 'ROHStation', 'POHStation',
              'Wagon1Number', 'Wagon1Type',
              'Wagon2Number', 'Wagon2Type',
              'Wagon3Number', 'Wagon3Type',
              'Wagon4Number', 'Wagon4Type',
              'Wagon5Number', 'Wagon5Type',
              'ModuleRecieveDate' ]


class SidingModuleListPageView(ListView):
    model = models.ModuleRecieved
    template_name = 'sidings/ModulesList.html'
    ordering = ['-Date']
    paginate_by = 50


class SidingModuleDetailPageView(DetailView):
    model = models.ModuleRecieved
    template_name = 'sidings/ModulesList_detail.html'


class SidingModuleEditView(UpdateView):
    model = models.ModuleRecieved
    fields = ['RakeNumber', 'BPC_Number',
              'LineNumber', 'ModuleName', 
              'ROHStation', 'POHStation',
              'Wagon1Number', 'Wagon1Type',
              'Wagon2Number', 'Wagon2Type',
              'Wagon3Number', 'Wagon3Type',
              'Wagon4Number', 'Wagon4Type',
              'Wagon5Number', 'Wagon5Type',
              'ModuleRecieveDate']
    template_name = 'sidings/ModulesList_edit.html'


class SidingModuleEditROHDateView(UpdateView):
    model = models.ModuleRecieved
    fields = ['ModuleROHDate', 'ModulePOHDate']
    template_name = 'sidings/ModulesList_edit.html'

class SidingModuleEditDefectView(UpdateView):
    model = models.ModuleRecieved
    fields = ['Wagon1Defect', 'Wagon2Defect',
              'Wagon3Defect', 'Wagon4Defect', 'Wagon5Defect', ]
    template_name = 'sidings/ModulesList_edit.html'


class SidingModuleEditDVSView(UpdateView):
    model = models.ModuleRecieved
    fields = ['ModuleDVS', 'ModuleDVR',  'ModuleDVSDate',
              'ModulePresentPosition', 'ModuleMadeFit',
              'ModuleMadeFitDateTime']
    template_name = 'sidings/ModulesList_edit.html'


class SidingModuleDeleteView(DeleteView):
    model = models.ModuleRecieved
    template_name = 'sidings/ModulesList_delete.html'
    success_url = reverse_lazy('siding_Modules_List')

def moduleName(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = models.ModuleRecieved.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(ModuleName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.ModuleName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)
            
    return render(request, 'sidings/ModulesList.html')


def RakeNumber(request):
    if request.is_ajax():
        if 'term' in request.GET:
            qs = models.ModuleRecieved.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(RakeNumber__icontains=itemTerm)
            print("resRAKE")
            print(res)
            Item = list()
            for product in res:
                if product.RakeNumber in Item:
                    pass
                else:
                    place_json = {}
                    place_json = product.RakeNumber
                    Item.append(place_json)
                    print("*------JsonResponse Start-----*")
                    print(Item)
                    print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

    return render(request, 'sidings/ModulesList.html')


def ModuleDetailLink(request):
    if request.method=='POST':
        ModuleName = request.POST.get('moduleName')
        print("ModuleName")
        print(ModuleName)
        qs = models.ModuleRecieved.objects.all()
        print("qs")
        print(qs)
        res = qs.filter(ModuleName=ModuleName)
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list' : res
        }
    return render(request, 'sidings/ModulesList.html', context)


def RakeDetailLink(request):
    if request.method == 'POST':
        RakeNumber = request.POST.get('RakeNumber')
        print("RakeNumber")
        print(RakeNumber)
        qs = models.ModuleRecieved.objects.all()
        print("qs")
        print(qs)
        res = qs.filter(RakeNumber=RakeNumber)
        res = res.order_by("ModuleROHDate")
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesList.html', context)
        

def DateDetailLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        print("date1")
        print(date1)
        print("date2")
        print(date2)
        qs = models.ModuleRecieved.objects.all()
        print("qs")
        print(qs)
        res = qs.filter(ModuleRecieveDate__range=[date1, date2])
        res = res.order_by("ModuleROHDate")
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesList.html', context)


def DateDetailGZBMUZLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='GZB_ICD_MUZ')
        res = res.order_by("-ModuleRecieveDate")
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListGZBMUZ.html', context)


def DateDetailGZBNOLILink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='GZB_ICD_NOLI')
        res = res.order_by("-ModuleRecieveDate")
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListGZBNOLI.html', context)


def DateDetailPNPBMDJLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='PNP_BMDJ')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListPNPBMDJ.html', context)


def DateDetailPNPDWNALink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='PNP_PCWD_DWNA')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListPNPDWNA.html', context)


def DateDetailSSBGHHLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='SSB_ICD_GHH')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListSSBGHH.html', context)


def DateDetailSSBPTTLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='SSB_ICD_PT')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListSSBPTT.html', context)


def DateDetailTKDACTLLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='TKD_ACTL')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListTKDACTL.html', context)


def DateDetailTKDHTPPLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='TKD_HTPP_PWL')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListTKDHTPP.html', context)


def DateDetailTKDICDLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[
                        date1, date2], ModulePresentPosition__icontains='TKD_ICD')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListTKDICD.html', context)


def DateDetailYardLink(request):
    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        qs = models.ModuleRecieved.objects.all()
        res = qs.filter(ModuleRecieveDate__range=[date1, date2], ModulePresentPosition__icontains='TKD_YARD')
        res = res.order_by("-ModuleRecieveDate")
        print("ordered List")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesListYard.html', context)

def TKDICDModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_ICD")
    res1 = res.filter(ModuleDVS=True).order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDICD.html', context)


def TKDICDModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_ICD")
    res = res.filter(ModuleDVS=True).order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDICD.html', context)


def TKDHTPPModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_HTPP_PWL").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDHTPP.html', context)


def TKDHTPPModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_HTPP_PWL").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDHTPP.html', context)



def TKDACTLModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_ACTL").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDACTL.html', context)


def TKDACTLModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_ACTL").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListTKDACTL.html', context)

def SSBGHHModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="SSB_ICD_GHH").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListSSBGHH.html', context)


def SSBGHHModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="SSB_ICD_GHH").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListSSBGHH.html', context)

def SSBPTTModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="SSB_ICD_PT").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListSSBGHH.html', context)


def SSBPTTModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="SSB_ICD_PT").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListSSBPTT.html', context)

def PNPBMDJModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="PNP_BMDJ").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListPNPBMDJ.html', context)


def PNPBMDJModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="PNP_BMDJ").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListPNPBMDJ.html', context)

def PNPDWNAModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="PNP_PCWD_DWNA").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListPNPDWNA.html', context)


def PNPDWNAModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="PNP_PCWD_DWNA")
    res = res.filter(ModuleDVS=True).order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListPNPDWNA.html', context)


def GZBNOLIModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="GZB_ICD_NOLI").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListGZBNOLI.html', context)


def GZBNOLIModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="GZB_ICD_NOLI").order_by('-Date')
    res = res.filter(ModuleDVS=True)
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListGZBNOLI.html', context)

def GZBMUZModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="GZB_ICD_MUZ").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListGZBMUZ.html', context)


def GZBMUZModuleListDVSPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="GZB_ICD_MUZ")
    res = res.filter(ModuleDVS=True).order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListGZBMUZ.html', context)

def YardModuleListPageView(request):
    qs = models.ModuleRecieved.objects.all()
    print("qs")
    print(qs)
    res = qs.filter(ModulePresentPosition="TKD_YARD").order_by('-Date')
    #print("qs")
    #print(qs)
    #res = qs.get(ModuleName=moduleName)
    print("res")
    print(res)
    context = {
        'object_list': res
    }
    return render(request, 'sidings/ModulesListYard.html', context)
