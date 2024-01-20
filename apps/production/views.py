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
    
class CompraView(View):
    form_class = CompraForm
    initial = {'key': 'value'}
    template_name = 'production/compra_register.html'

    def get(self, request):

        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form': self.form_class})
    
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'compra criada com sucesso')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})
   
class CompraList(ListView):
    model = Compra
    queryset = Compra.objects.all()
    template_name = 'production/compra_list.html'
    paginate_by = 5
    
class EstoqueView(ListView):
    model = EstoqueFruta
    queryset = EstoqueFruta.objects.all()
    template_name = 'production/estoque_list.html'