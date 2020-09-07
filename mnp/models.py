from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class mnpPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = models.FileField(
        upload_to='uploadsMnp/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mnppost-detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class mnpComment(models.Model):
    post = models.ForeignKey( mnpPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    upload = models.FileField(upload_to='uploadsMnpComments/%Y/%m/%d/', blank=True, null=True)
    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('mnppost-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.text
