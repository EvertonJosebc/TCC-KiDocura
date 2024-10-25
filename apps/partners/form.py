from django.forms import forms
from django.forms import ModelForm
from.models import Cliente, Produtor
from django.core.exceptions import ValidationError


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
        
    def clean_email(self):
        Email = self.cleaned_data.get("email")
        if Cliente.objects.filter(email=Email).exists():
            raise ValidationError("Este email já está cadastrado!")
        return Email
    
    def clean_CNPJ(self):
        cnpj = self.cleaned_data.get("CNPJ")
        if Cliente.objects.filter(CNPJ=cnpj).exists():
            raise ValidationError("Este CNPJ já está cadastrado!")
        return cnpj
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
        
    def clean_email(self):
        Email = self.cleaned_data.get("email")
        if Produtor.objects.filter(email=Email).exists():
            raise ValidationError("Este email já está cadastrado!")
        return Email
    
    def clean_CPF(self):
        cpf = self.cleaned_data.get("CPF")
        if Produtor.objects.filter(CPF=cpf).exists():
            raise ValidationError("Este CPF já está cadastrado!")
        return cpf