from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sidingz import models
from django.urls import reverse_lazy
# from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class SidingHomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'sidings_home.html'


class SidingICDOkhlaHomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'sidings/ICD_Okhla_home.html'



class SidingModuleRecievedPageView(LoginRequiredMixin, CreateView):
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
              'ModuleRecieveDate', 'ModuleDVS',
              'ModuleDVR', 'ModuleMadeFit']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SidingModuleListPageView(LoginRequiredMixin, ListView):
    model = models.ModuleRecieved
    template_name = 'sidings/ModulesList.html'
    ordering = ['-Date']
    paginate_by = 50


class SidingModuleDetailPageView(LoginRequiredMixin, DetailView):
    model = models.ModuleRecieved
    template_name = 'sidings/ModulesList_detail.html'


class SidingModuleEditView(LoginRequiredMixin, UpdateView):
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


class SidingModuleEditROHDateView(LoginRequiredMixin, UpdateView):
    model = models.ModuleRecieved
    fields = ['ModuleROHDate', 'ModulePOHDate']
    template_name = 'sidings/ModulesList_edit.html'


class SidingModuleEditDefectView(LoginRequiredMixin, UpdateView):
    model = models.ModuleRecieved
    fields = ['Wagon1Defect', 'Wagon2Defect',
              'Wagon3Defect', 'Wagon4Defect', 'Wagon5Defect', ]
    template_name = 'sidings/ModulesList_edit.html'


class SidingModuleEditDVSView(LoginRequiredMixin, UpdateView):
    model = models.ModuleRecieved
    fields = ['ModuleDVS', 'ModuleDVR',  'ModuleDVSDate',
              'ModulePresentPosition', 'ModuleMadeFit',
              'ModuleMadeFitDateTime']
    template_name = 'sidings/ModulesList_edit.html'


class SidingModuleEditROHFileView(LoginRequiredMixin, UpdateView):
    model = models.ModuleRecieved
    fields = ['ROHFile']
    template_name = 'sidings/ModulesList_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SidingModuleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ModuleRecieved
    template_name = 'sidings/ModulesList_delete.html'
    success_url = reverse_lazy('siding_Modules_List')


@login_required
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


@login_required
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


@login_required
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


@login_required
def RakeDetailLink(request):
    if request.method == 'POST':
        RakeNumber = request.POST.get('RakeNumber')
        print("RakeNumber")
        print(RakeNumber)
        qs = models.ModuleRecieved.objects.all()
        print("qs")
        print(qs)
        res = qs.filter(RakeNumber=RakeNumber)
        res = res.order_by("-ModuleROHDate")
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesList.html', context)
        

@login_required
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
        res = res.order_by("-ModuleROHDate")
        #print("qs")
        #print(qs)
        #res = qs.get(ModuleName=moduleName)
        print("res")
        print(res)
        context = {
            'object_list': res
        }
    return render(request, 'sidings/ModulesList.html', context)


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
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
