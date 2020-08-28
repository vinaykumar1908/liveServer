from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ROH import models
from sidingz import models as sm
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'ROH_home.html'

class RegisterView(TemplateView):
    template_name = 'ROH/Registers.html'

# Views for Wheel Recieved from Judw Register start
class registerWheelRecievedJudwListView(ListView):
    model = models.registerWheelRecievedJudw
    template_name = 'ROH/registerWheelRecievedJudw/registerWheelRecievedJudw.html'
    ordering = ['-id']
    paginate_by = 10

class registerWheelRecievedJudwCreateView(CreateView):
    model =  models.registerWheelRecievedJudw
    template_name = 'ROH/registerWheelRecievedJudw/registerWheelRecievedJudw_new.html' 
    fields = '__all__'

class registerWheelRecievedJudwDetailView(DetailView): 
    model = models.registerWheelRecievedJudw 
    template_name = 'ROH/registerWheelRecievedJudw/registerWheelRecievedJudw_detail.html'

class registerWheelRecievedJudwEditView(UpdateView): 
    model = models.registerWheelRecievedJudw
    fields = '__all__' 
    template_name = 'ROH/registerWheelRecievedJudw/registerWheelRecievedJudw_edit.html'

class registerWheelRecievedJudwDeleteView(DeleteView): 
    model = models.registerWheelRecievedJudw 
    template_name = 'ROH/registerWheelRecievedJudw/registerWheelRecievedJudw_delete.html' 
    success_url = reverse_lazy('WRJudwR')
# Views for Wheel Recieved from Judw Register end

# Views for Wheel Dispatched from Judw Register start
class registerWheelDispatchedJudwListView(ListView):
    model = models.registerWheelDispatchedJudw
    template_name = 'ROH/registerWheelDispatchedJudw/registerWheelDispatchedJudw.html'
    ordering = ['-id']
    paginate_by = 10

class registerWheelDispatchedJudwCreateView(CreateView):
    model =  models.registerWheelDispatchedJudw
    template_name = 'ROH/registerWheelDispatchedJudw/registerWheelDispatchedJudw_new.html' 
    fields = '__all__'

class registerWheelDispatchedJudwDetailView(DetailView): 
    model = models.registerWheelDispatchedJudw 
    template_name = 'ROH/registerWheelDispatchedJudw/registerWheelDispatchedJudw_detail.html'

class registerWheelDispatchedJudwEditView(UpdateView): 
    model = models.registerWheelDispatchedJudw
    fields = '__all__' 
    template_name = 'ROH/registerWheelDispatchedJudw/registerWheelDispatchedJudw_edit.html'

class registerWheelDispatchedJudwDeleteView(DeleteView): 
    model = models.registerWheelDispatchedJudw 
    template_name = 'ROH/registerWheelDispatchedJudw/registerWheelDispatchedJudw_delete.html' 
    success_url = reverse_lazy('WDJudwR')
# Views for Wheel Dispatched from Judw Register end

# Views for Hot Axle Wagon Register start
class registerHotAxleWagonListView(ListView):
    model = models.registerHotAxle_Wagon
    template_name = 'ROH/registerHotAxleWagon/registerHotAxleWagon.html'
    ordering = ['-id']
    paginate_by = 10

class registerHotAxleWagonCreateView(CreateView):
    model =  models.registerHotAxle_Wagon
    template_name = 'ROH/registerHotAxleWagon/registerHotAxleWagon_new.html' 
    fields = '__all__'

class registerHotAxleWagonDetailView(DetailView): 
    model = models.registerHotAxle_Wagon 
    template_name = 'ROH/registerHotAxleWagon/registerHotAxleWagon_detail.html'

class registerHotAxleWagonEditView(UpdateView): 
    model = models.registerHotAxle_Wagon
    fields = '__all__' 
    template_name = 'ROH/registerHotAxleWagon/registerHotAxleWagon_edit.html'

class registerHotAxleWagonDeleteView(DeleteView): 
    model = models.registerHotAxle_Wagon 
    template_name = 'ROH/registerHotAxleWagon/registerHotAxleWagon_delete.html' 
    success_url = reverse_lazy('HAWR')
# Views for Hot Axle Wagon Register end

# Views for Gauge Calibration Register start

class registerGaugeCalibrationListView(ListView):
    model = models.registerGaugeCalibration
    template_name = 'ROH/registerGaugeCalibration/registerGaugeCalibration.html'
    ordering = ['-id']
    paginate_by = 10

class registerGaugeCalibrationCreateView(CreateView):
    model =  models.registerGaugeCalibration
    template_name = 'ROH/registerGaugeCalibration/registerGaugeCalibration_new.html' 
    fields = '__all__'

class registerGaugeCalibrationDetailView(DetailView): 
    model = models.registerGaugeCalibration 
    template_name = 'ROH/registerGaugeCalibration/registerGaugeCalibration_detail.html'

class registerGaugeCalibrationEditView(UpdateView): 
    model = models.registerGaugeCalibration
    fields = ['NextCalibrationDue'] 
    template_name = 'ROH/registerGaugeCalibration/registerGaugeCalibration_edit.html'

class registerGaugeCalibrationDeleteView(DeleteView): 
    model = models.registerGaugeCalibration 
    template_name = 'ROH/registerGaugeCalibration/registerGaugeCalibration_delete.html' 
    success_url = reverse_lazy('GC')

# Views for Gauge Calibration Register end


def ROHModules(request):
    qs = sm.ModuleRecieved.objects.all().filter(ModuleDVR=True)
    print(qs)
    qs = qs.order_by('-Date')
    context = {
        'obj': qs
    }

    return render(request, 'ROH/ROHModules.html', context)
