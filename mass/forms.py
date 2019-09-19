from django.forms import ModelForm
from .models import Mass
class MassForm(ModelForm):
    class Meta:
        model = Mass
        fields=['day', 'startTime', 'intention', 'surname', 'email']
