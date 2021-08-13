from django.forms import ModelForm

import letters
from letters.models import Letter


class CreateLetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = ['name','image','description']
