from django.forms import ModelForm
from .models import mnpComment, mnpPost


class CommentForm(ModelForm):
    
    class Meta:
        model = mnpComment
        fields = ('text','upload')
