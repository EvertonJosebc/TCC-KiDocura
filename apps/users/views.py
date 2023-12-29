from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from rolepermissions.roles import assign_role
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import User
from .form import RegisterForm

# Create your views here.

    
class Home(LoginRequiredMixin,TemplateView):
    template_name = "users/dashboard.html"
    
class Register(View):
    form_class = RegisterForm
    initial = {"key": "value"}
    template_name = "users/register.html"

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': self.form_class})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            tipoUsuario = form.cleaned_data.get("tipoUsuario")
            email = form.cleaned_data.get("email")
            user = User.objects.get(email=email)
            if tipoUsuario == "gerente":
                assign_role(user,'gerente')
                
            if tipoUsuario == "entregador":
                assign_role(user,'entregador')
                
            if tipoUsuario == "tec. alimentos":
                assign_role(user,'tec. alimentos')
                
            if tipoUsuario == "ger. de producao":
                assign_role(user,'ger. de producao')
                
            if tipoUsuario == "aux. de producao":
                assign_role(user,'aux. de producao')
                
            username = form.cleaned_data.get("username")
            RG = form.cleaned_data.get("RG")
            CPF = form.cleaned_data.get("CPF")
            telefone = form.cleaned_data.get("telefone")
            rua = form.cleaned_data.get("rua")
            bairro = form.cleaned_data.get("bairro")
            cidade = form.cleaned_data.get("cidade")
            CEP = form.cleaned_data.get("CEP")
            messages.success(request, f"Account created for {username}")
            return redirect(to="/")
        return render(request, self.template_name, {'form': form})

class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard")

    def form_invalid(self, form):
        messages.error(self.request, "Inválido Login e Senha.")
        return self.render_to_response(self.get_context_data(form=form))
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
    
class AdminUsers(LoginRequiredMixin,ListView):
    model = User
    context_object_name = 'user_list'
    paginate_by = 10

class UsersUpdate(UpdateView):
    model = User
    fields = ['username', 'email', 'rua', 'bairro', 'cidade', 'CEP', 'telefone', 'tipoUsuario']
    template_name = 'users/user_update.html'
    success_url = reverse_lazy("dashboard")
    
class UserDetail(DetailView):
    model = User
    def client_detail_view(request, pk):
        user = get_object_or_404(User, pk=pk)
        return render(request, 'users/user_detail.html', context={'user': user})
