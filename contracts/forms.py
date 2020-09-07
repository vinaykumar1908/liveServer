from django.forms import ModelForm
from .models import ContractComment, ContractPost


class CommentForm(ModelForm):

    class Meta:
        model = ContractComment
        fields = ('text','commentfile')
