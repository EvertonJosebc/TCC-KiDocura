from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView

# Create your views here.

from .models import Produtor, Cliente
from .form import ProdutorForm, ClienteForm

class ClienteView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'partners/cliente_register.html'
    success_url = reverse_lazy("dashboard")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "O cliente foi Cadastrado")
        return super(ClienteView,self).form_valid(form)
    
class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'partners/client_list.html'
    paginate_by = 10
    
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome', 'rua', 'bairro', 'cidade', 'CEP', 'telefone', 'email']
    template_name = 'partners/client_update.html'
    success_url = reverse_lazy("dashboard")
    
class ClienteDetail(DetailView):
    model = Cliente
    def client_detail_view(request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        return render(request, 'partners/cliente_detail.html', context={'cliente': cliente})
    
class ProdutorView(CreateView):
    model = Produtor
    form_class = ProdutorForm
    template_name = 'partners/produtor_register.html'
    success_url = reverse_lazy("dashboard")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "O Produtor foi Cadastrado")
        return super(ProdutorView,self).form_valid(form)
    
class ProdutorList(ListView):
    model = Produtor
    queryset = Produtor.objects.all()
    template_name = 'partners/produtor_list.html'
    
class ProdutorUpdate(UpdateView):
    model = Produtor
    fields = ['nome', 'rua', 'bairro', 'cidade', 'CEP', 'telefone', 'email']
    template_name = 'partners/produtor_update.html'
    success_url = reverse_lazy("dashboard")
    
class ProdutorDetail(DetailView):
    model = Produtor
    def client_detail_view(request, pk):
        produtor = get_object_or_404(produtor, pk=pk)
        return render(request, 'partners/produtor_detail.html', context={'produtor': produtor})