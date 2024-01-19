from django.forms import forms
from django.forms import ModelForm
from .models import Fruta, Compra, EstoqueFruta
from django.core.exceptions import ValidationError

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

class CompraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Compra
        fields = [
            "quantidade",
            "fruta",
            "produtor",
            "espaco_estoque",
        ]
        
        def clean_espaco_estoque(self):
            espaco_estoque = self.cleaned_data['espaco_estoque']
            estoque = EstoqueFruta.objects.all()
            print(estoque)
            if len(estoque) == 0:
                if espaco_estoque < 50:
                    estoque = EstoqueFruta.objects.create(quantidade_atual = espaco_estoque)
                    estoque.save()
                    
                else:
                    raise ValidationError('O estoque não suporta a quantidade inserida!')
            
            else:
                if espaco_estoque + estoque[0].quantidade_atual >estoque[0].quantidade_max:
                    raise ValidationError('O estoque não suporta a quantidade inserida!')
                
            return espaco_estoque
                    
            
            