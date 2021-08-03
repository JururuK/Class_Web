from django.forms import ModelForm

from articles.models import Article


class CreateArticleForm(ModelForm):
    class Meta :
        model = Article
        fields = ['title','image','content']