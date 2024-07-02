from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from braces.views import GroupRequiredMixin
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
from django.http import FileResponse
from django.db.models import Sum

# Create your views here.

from apps.production.models import Compra
from .models import Produtor, Cliente
from .form import ProdutorForm, ClienteForm

class ClienteView(GroupRequiredMixin, CreateView):
    group_required = u'gerente'
    model = Cliente
    form_class = ClienteForm
    template_name = 'partners/cliente_register.html'
    success_url = reverse_lazy("dashboard")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "O cliente foi Cadastrado")
        return super(ClienteView,self).form_valid(form)
    
class ClienteList(GroupRequiredMixin, ListView):
    group_required = u'gerente'
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'partners/client_list.html'
    paginate_by = 10
    
class ClienteUpdate(GroupRequiredMixin, UpdateView):
    group_required = u'gerente'
    model = Cliente
    fields = ['nome', 'rua', 'bairro', 'cidade', 'CEP', 'telefone', 'email']
    template_name = 'partners/client_update.html'
    success_url = reverse_lazy("dashboard")
    
class ClienteDetail(GroupRequiredMixin, DetailView):
    group_required = u'gerente'
    model = Cliente
    def client_detail_view(request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        return render(request, 'partners/cliente_detail.html', context={'cliente': cliente})
    
class ProdutorView(GroupRequiredMixin, CreateView):
    group_required = [u'gerente', u'tecdealimentos']
    model = Produtor
    form_class = ProdutorForm
    template_name = 'partners/produtor_register.html'
    success_url = reverse_lazy("dashboard")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "O Produtor foi Cadastrado")
        return super(ProdutorView,self).form_valid(form)
    
class ProdutorList(GroupRequiredMixin, ListView):
    group_required = [u'gerente', u'tecdealimentos']
    model = Produtor
    queryset = Produtor.objects.all()
    template_name = 'partners/produtor_list.html'
    
class ProdutorUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'gerente', u'tecdealimentos']
    model = Produtor
    fields = ['nome', 'rua', 'bairro', 'cidade', 'CEP', 'telefone', 'email']
    template_name = 'partners/produtor_update.html'
    success_url = reverse_lazy("dashboard")
    
class ProdutorDetail(GroupRequiredMixin, DetailView):
    group_required = [u'gerente', u'tecdealimentos']
    model = Produtor
    context_object_name = 'produtor'
    template_name = 'partners/produtor_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productions = Compra.objects.filter(produtor = self.kwargs.get("pk"))
        productions2 = Compra.objects.filter(produtor = self.kwargs.get("pk")).values('fruta').annotate(total_quantidade=Sum('quantidade'))
        
        labels = [obj['fruta'] for obj in productions2]
        values = [obj['total_quantidade'] for obj in productions2]
           
        context['productions'] = productions
        context['labels'] = labels
        context['values'] = values
        
        return context
    