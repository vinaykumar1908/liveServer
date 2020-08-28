from django.db import models
from django.urls import reverse
# Create your models here.
class registerWheelRecievedJudw(models.Model):
    Date = models.DateField(blank=True)
    TruckNo = models.CharField(max_length=12)
    BLC = models.IntegerField()
    BCN = models.IntegerField()
    ICF = models.IntegerField()
    Remark = models.TextField()
    def __str__(self):
        return str(self.Date)
    def get_absolute_url(self):
        return reverse('WRJudwR')
class registerWheelDispatchedJudw(models.Model):
    Date = models.DateField(blank=True)
    TruckNo = models.CharField(max_length=12)
    BLC = models.IntegerField()
    BCN = models.IntegerField()
    ICF = models.IntegerField()
    Remark = models.TextField()
    def __str__(self):
        return str(self.Date)
    def get_absolute_url(self):
        return reverse('WDJudwR')
class registerHotAxle_Wagon(models.Model):
    DateDetached = models.DateField(blank=True)
    Station = models.CharField(max_length=5)
    Section = models.CharField(max_length=5)
    WagonNumber = models.BigIntegerField()
    Railway = models.CharField(max_length=5)
    Class = models.CharField(max_length=5)
    TruckNo = models.CharField(max_length=12)
    WheelRecieveDate = models.DateField()
    Remark = models.TextField()
    def __str__(self):
        return str(self.DateDetached)
    def get_absolute_url(self):
        return reverse('HAWR')
class registerGaugeCalibration(models.Model):
    Description = models.CharField(max_length=50)
    IMTENumber = models.CharField(max_length=15)
    NextCalibrationDue = models.DateField()
    def __str__(self):
        return self.Description
    def get_absolute_url(self):
        return reverse('GC')
