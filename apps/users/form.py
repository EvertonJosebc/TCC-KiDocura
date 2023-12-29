from django.forms import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

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