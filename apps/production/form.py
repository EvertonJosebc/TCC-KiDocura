from django.forms import forms
from django.forms import ModelForm
from .models import Fruta, Compra, EstoqueFruta, Producao, EstoquePolpa, Entrega
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
            if espaco_estoque <= 50:
                estoque = EstoqueFruta.objects.create(quantidade_atual = espaco_estoque)
                estoque.save()
                
            else:
                raise ValidationError('O estoque não suporta a quantidade inserida!')
        
        else:
            if espaco_estoque + estoque[0].quantidade_atual >estoque[0].quantidade_max:
                raise ValidationError('O estoque não suporta a quantidade inserida!')
            
            estoque[0].quantidade_atual += espaco_estoque
            estoque[0].save()
        return espaco_estoque
                    
            
class ProducaoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProducaoForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Producao
        fields = [
            "quantidade_produzida",
            "fruta",
            "quantidade_reduzida",
        ]
        
    def clean_quantidade_reduzida(self):
        quantidade_reduzida = self.cleaned_data['quantidade_reduzida']
        estoque = EstoqueFruta.objects.all()
        if len(estoque) > 0:
            if estoque[0].quantidade_atual - quantidade_reduzida <= 0:
                raise ValidationError('O estoque não tem essa quantidade de produtos disponíveis!')
            
            estoque[0].quantidade_atual -= quantidade_reduzida
            estoque[0].save()
            
        else:
            raise ValidationError('O estoque não tem essa quantidade de produtos disponíveis!')
        
        return quantidade_reduzida     
    
    def clean_quantidade_produzida(self):
        quantidade_produzida = self.cleaned_data['quantidade_produzida']
        estoquep = EstoquePolpa.objects.all()
        print(estoquep)
        if len(estoquep) == 0:
            if quantidade_produzida <= 1000:
                estoquep = EstoquePolpa.objects.create(quantidade_atual = quantidade_produzida)
                estoquep.save()
                
            else:
                raise ValidationError('O estoquep não suporta a quantidade inserida!')
        
        else:
            if quantidade_produzida + estoquep[0].quantidade_atual >estoquep[0].quantidade_max:
                raise ValidationError('O estoquep não suporta a quantidade inserida!')
            
            estoquep[0].quantidade_atual += quantidade_produzida
            estoquep[0].save()
        return quantidade_produzida
    
class EntregaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntregaForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Entrega
        fields = [
            "quantidade_entregue",
            "cliente",
        ]
        
    def clean_quantidade_entregue(self):
        quantidade_entregue = self.cleaned_data['quantidade_entregue']
        estoque = EstoquePolpa.objects.all()
        if len(estoque) > 0:
            if estoque[0].quantidade_atual - quantidade_entregue <= 0:
                raise ValidationError('O estoque não tem essa quantidade de produtos disponíveis!')
            
            estoque[0].quantidade_atual -= quantidade_entregue
            estoque[0].save()
            
        else:
            raise ValidationError('O estoque não tem essa quantidade de produtos disponíveis!')
        
        return quantidade_entregue