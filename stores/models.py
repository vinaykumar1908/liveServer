from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.

#class Item(models.Model):
#    Item = models.CharField(primary_key=True, null=False, default=" ", max_length=100,)
#    def __str__(self):
#        return str(self.Item)

class registerCurrentStock(models.Model):
    #Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    Item = models.CharField(unique=True, max_length=100)
    PL_Number = models.BigIntegerField(unique=True, null=False)
    AAC = models.IntegerField(null=False, default=0)
    Stock = models.IntegerField()
    updateTime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.Item)
    def get_absolute_url(self):
        return reverse('CSR')

class registerStockRecieved(models.Model):
    STOCK_REC_CHOICES = ( 
    ("AMM", "AMM"), 
    ("JAGADHRI", "JAGADHRI"), 
    ("SHAKURBASTI", "SHAKURBASTI"),
    ) 
    Item = models.CharField(max_length=100)
    #Item = models.ForeignKey(registerCurrentStock, to_field='Item', on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_item')
    AAC = models.IntegerField(null=False, default=0)
    pl_Number = models.IntegerField()
    stockRecieved = models.IntegerField(null=False)
    stockRecievedChoices = models.CharField(max_length=11, choices = STOCK_REC_CHOICES, default = 'AMM')
    updateTime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.Item)
    def get_absolute_url(self):
        return reverse('SRR')

class registerStockDispatchedROH(models.Model):
    Item = models.CharField(max_length=100)
    #Item = models.ForeignKey(registerCurrentStock, on_delete=models.CASCADE)
    PL_Number = models.IntegerField()
    stockDispatched = models.IntegerField(null=False)
    updateTime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.Item)

class registerStockDispatchedSickline(models.Model):
    Item = models.CharField(max_length=100)
    #Item = models.ForeignKey(registerCurrentStock, on_delete=models.CASCADE)
    PL_Number = models.IntegerField()
    stockDispatched = models.IntegerField(null=False)
    updateTime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.Item)

class registerStockDispatchedYard(models.Model):
    YARD_CHOICES = ( 
    ("ACTL", "ACTL"), 
    ("HTPP", "HTPP"), 
    ("ICD_TKD", "ICD_TKD"), 
    ("ICD", "ICD"),
    ) 
    Item = models.CharField(max_length=100)
    #Item = models.ForeignKey(registerCurrentStock, on_delete=models.CASCADE)
    PL_Number = models.IntegerField()
    stockDispatched = models.IntegerField(null=False)
    Yard = models.CharField(max_length=7, choices = YARD_CHOICES, default = 'ACTL')
    updateTime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.Item)

class registerStockDispatchedTrainDuty(models.Model):
    Item = models.CharField(max_length=100)
   # Item = models.ForeignKey(registerCurrentStock, on_delete=models.CASCADE)
    PL_Number = models.IntegerField()
    stockDispatched = models.IntegerField(null=False)
    updateTime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.Item)
