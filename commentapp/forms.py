from django.forms import ModelForm

from commentapp.models import Comment


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']