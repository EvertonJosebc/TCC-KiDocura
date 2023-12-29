from django.forms import forms
from django.forms import ModelForm
from.models import Cliente, Produtor


class ClienteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Cliente
        fields = [
            "nome",
            "rua",
            "bairro",
            "cidade",
            "CEP",
            "telefone",
            "email",
            "CNPJ"
        ]
        
class ProdutorForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProdutorForm, self).__init__(*args, **kwargs)
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Produtor
        fields = [
            "nome",
            "rua",
            "bairro",
            "cidade",
            "CEP",
            "telefone",
            "email",
            "CPF"
        ]