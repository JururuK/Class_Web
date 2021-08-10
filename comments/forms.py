from django.forms import ModelForm

from comments.models import Comment


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']