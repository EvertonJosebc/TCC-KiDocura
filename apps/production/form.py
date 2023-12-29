from django.forms import forms
from django.forms import ModelForm
from .models import Fruta

class FrutaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FrutaForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Fruta
        fields = [
            "nome",
            "preco",
            "condicao",
        ]