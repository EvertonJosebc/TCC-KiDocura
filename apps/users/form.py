from django.forms import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =[
            "username",
            "email",
            "RG",
            "CPF",
            "telefone",
            "tipoUsuario",
            "rua",
            "bairro",
            "cidade",
            "CEP",
            "password1",
            "password2",
        ]
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    def clean_username(self):
        Username = self.cleaned_data.get("username")
        if User.objects.filter(username=Username).exists():
            raise ValidationError("Este nome já está cadastrado!")
        return Username
    
    def clean_email(self):
        Email = self.cleaned_data.get("email")
        if User.objects.filter(email=Email).exists():
            raise ValidationError("Este email já está cadastrado!")
        return Email
    
    def clean_RG(self):
        rg = self.cleaned_data.get("RG")
        if User.objects.filter(RG=rg).exists():
            raise ValidationError("Este RG já está cadastrado!")
        return rg
    
    def clean_CPF(self):
        cpf = self.cleaned_data.get("CPF")
        if User.objects.filter(CPF=cpf).exists():
            raise ValidationError("Este CPF já está cadastrado!")
        return cpf