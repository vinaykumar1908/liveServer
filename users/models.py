from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    DesignationChoices = (

        ("SSE/C&W/TKD", "SSE/C&W/TKD"),
        ("JE/C&W/TKD", "JE/C&W/TKD"),
        ("Techical Asst", "Technical Asst"),
    )
    PlaceOfPosting = (
        ("TKD Sickline Office", "TKD Sickline Office"),
        ("TKD ROH Office", "TKD ROH"),
        ("TKD SSE Planning Office", "TKD SSE Planning Office"),
        ("TKD M&P Section", "TKD M&P Section"),
        ("TKD Administration", "TKD Administration"),
        ("TKD Stores", "TKD Stores"),
        ("TKD Wheel Lathe", "TKD Wheel Lathe"),
        ("TKD Train Duty Office", "TKD Train Duty Office"),
        ("TKD ICD", "TKD ICD"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Mobile = models.BigIntegerField(null=True, blank=True)
    LocalAddress = models.TextField(null=True, blank=True)
    IDNumber = models.CharField(max_length=30, default='ID Number', null=True)
    Designation = models.CharField(max_length=30, default='JE/C&W/TKD', null=True, blank=True)
    Posted = models.CharField(max_length=30, choices=PlaceOfPosting, default='TKD Administration', null=True, blank=True)
    DateOfJoining = models.DateField(null=True, default='1001-01-01', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        else:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
