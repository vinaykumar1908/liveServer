from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class ModuleRecieved(models.Model):
    WAGON_TYPE_CHOICES = ( 
        ("SelectWagon", "Please Select Wagon Type"),  
        ("BOXN", "BOXN"),
        ("BOXNHA", "BOXNHA"),
        ("BOXNHS", "BOXNHS"),
        ("BOXNCR", "BOXNCR"),
        ("BOXNLW", "BOXNLW"), 
        ("BOXNB", "BOXNB"),
        ("BOXNF", "BOXNF"),
        ("BOXNG", "BOXNG"),
        ("BOY", "BOY"),
        ("BOST", "BOST"),
        ("BOXNAL", "BOXNAL"),
        ("BOSTHS", "BOSTHS"),
        ("BOXNHL", "BOXNHL"),
        ("BOXNAL", "BOXNAL"),
        ("BOXNS", "BOXNS"),
        ("BCN", "BCN"),
        ("BCNA", "BCNA"),
        ("BCNAHS", "BCNAHS"),
        ("BCCNR", "BCCNR"),
        ("BTPN", "BTPN"),
        ("BTPNHS", "BTPNHS"),
        ("BTPGLN", "BTPGLN"),
        ("BTALN", "BTALN"),
        ("BTCS", "BTCS"),
        ("BTPH", "BTPH"),
        ("BTAP", "BTAP"),
        ("BTFLN", "BTFLN"),
        ("BRNA", "BRNA"),
        ("BRNAHS", "BRNAHS"),
        ("BFNS", "BFNS"),
        ("BOMN", "BOMN"),
        ("BRSTH", "BRSTH"),
        ("BFAT", "BFAT"),
        ("BLCA", "BLCA"),
        ("BLCB", "BLCB"),
        ("BLLA", "BLLA"),
        ("BLLB", "BLLB"),
        ("BRS", "BRS"),
        ("BFU", "BFU"),
        ("BRHNEHS", "BRHNEHS"),
        ("BCL", "BCL"), 
        ("BCLA", "BCLA"),
        ("BOBYN", "BOBYN"),
        ("BOBYNHS", "BOBYNHS"),
        ("BOBRN", "BOBRN"),
        ("BOBRNHS", "BOBRNHS"),
        ("BOBRAL", "BOBRAL"),
        ("BOBSN", "BOBSN"),
        ("BWTB", "BWTB"),
        ("MBWT", "MBWT"),
        ("DBKM", "DBKM"),
        ("MBWZ", "MBWZ"),
        ("BVZC", "BVZC"),
        ("BVZI", "BVZI"),
        ("BFKHN", "BFKHN"),
    ) 
    LINENUMBER_CHOICES = (
        ("SELECTLINE", "Please Select Examination Line"),
        ("NH1", "NH1"),
        ("NH2", "NH2"),
        ("NH3", "NH3"),
        ("NH4", "NH4"),
        ("NH5", "NH5"),
        ("NH6", "NH6"),
        ("NH7", "NH7"),
    )
    MODULE_PRESENT_POSITION = (
        ("TKD_ROH1", "TKD ROH 1"),
        ("TKD_ROH2", "TKD ROH 2"),
        ("TKD_Sickline", "TKD Sickline"),
        ("TKD_ACTL", "TKD ACTL"),
        ("TKD_HTPP_PWL", "TKD HTPP PWL"),
        ("TKD_ICD", "TKD ICD"),
        ("TKD_YARD", "TKD YARD"),
        ("SSB_ICD_GHH", "SSB ICD GHH"),
        ("SSB_ICD_PT", "SSB ICD PTT"),
        ("GZB_ICD_NOLI", "GZB ICD NOLI"),
        ("GZB_ICD_MUZ", "GZB ICD MUZ"),
        ("PNP_BMDJ", "PNP BMDJ"),
        ("PNP_PCWD_DWNA", "PNP PCWD DWNA"),
    )
    Serial = models.AutoField(primary_key=True)
    Date = models.DateTimeField(default=timezone.now)
    RakeNumber = models.CharField(max_length=50, null=True)
    BPC_Number = models.BigIntegerField(null=True)
    LineNumber = models.CharField(
        max_length=10, choices=LINENUMBER_CHOICES, default='SELECTLINE', null=True, blank=True)
    ModuleName = models.CharField(max_length=20, null=True)
    Wagon1Number = models.BigIntegerField(null=True, blank=True)
    Wagon1Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon2Number = models.BigIntegerField(null=True, blank=True)
    Wagon2Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon3Number = models.BigIntegerField(null=True, blank=True)
    Wagon3Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon4Number = models.BigIntegerField(null=True, blank=True)
    Wagon4Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon5Number = models.BigIntegerField(null=True, blank=True)
    Wagon5Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    ModuleRecieveDate = models.DateField(null=True, default='1001-01-01')
    ModuleCommDate = models.DateField(null=True, default='1001-01-01', blank=True)
    ModuleROHDate = models.DateField(null=True, default='1001-01-01', blank=True)
    ModulePOHDate = models.DateField(null=True, default='1001-01-01', blank=True)
    Wagon1Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon2Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon3Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon4Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon5Defect = models.CharField(
        max_length=100, null=True, blank=True)
    ModuleDVS = models.BooleanField(default=False, blank=True)
    ModuleDVR = models.BooleanField(default=False, blank=True)
    ModuleDVSDate = models.DateField(null=True, blank=True)
    POHStation = models.CharField(max_length = 100, null = True, blank = True)
    ROHStation = models.CharField(max_length=100, null=True, blank=True)
    ModulePresentPosition = models.CharField(
        max_length=13, choices=MODULE_PRESENT_POSITION, default='YARD', null=False)
    ModuleMadeFit = models.BooleanField(default=False, blank=True)
    ModuleMadeFitDateTime = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ROHFile = models.FileField(upload_to='ROH/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return str(self.ModuleName)
    def get_absolute_url(self):
        return reverse('Modules_detail', kwargs={'pk': self.pk})
    


