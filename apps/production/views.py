from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from .models import Fruta, Compra, EstoqueFruta
from .form import FrutaForm, CompraForm

# Create your views here.

class FrutaView(CreateView):
    model = Fruta
    form_class = FrutaForm
    template_name = 'production/fruta_register.html'
    success_url = reverse_lazy("dashboard")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "A fruta foi Cadastrada")
        return super(FrutaView,self).form_valid(form)
    
class FrutaList(ListView):
    model = Fruta
    queryset = Fruta.objects.all()
    template_name = 'production/fruta_list.html'
    paginate_by = 5
    
class FrutaUpdate(UpdateView):
    model = Fruta
    fields = ['nome', 'preco', 'condicao']
    template_name = 'production/fruta_update.html'
    success_url = reverse_lazy("dashboard")
    
class CompraView(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'production/compra_register.html'
    success_url = reverse_lazy("production:compra_register")
    
    def form_valid(self, form):
            form.instance.user = self.request.user
            form.save()
            return super(CompraView,self).form_valid(form)
   
    # def form_invalid(self, form):
    #     messages.error(self.request, "Inválido Login e Senha.")
    #     return self.render_to_response(self.get_context_data(form=form))
    
class CompraList(ListView):
    model = Compra
    queryset = Compra.objects.all()
    template_name = 'production/compra_list.html'
    paginate_by = 5
    

class EstoqueView(ListView):
    model = EstoqueFruta
    queryset = EstoqueFruta.objects.all()
    template_name = 'production/estoque_list.html'