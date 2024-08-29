from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, TemplateView
from django.http import JsonResponse
from django.db.models import F, Case, Value, When, BooleanField
from braces.views import GroupRequiredMixin

from .models import Fruta, Compra, EstoqueFruta, Producao, EstoquePolpa, Entrega
from .form import FrutaForm, CompraForm, ProducaoForm, EntregaForm

# Create your views here.

class FrutaView(GroupRequiredMixin, CreateView):
    group_required = [u'gerente', u'tecdealimentos']
    model = Fruta
    form_class = FrutaForm
    template_name = 'production/fruta_register.html'
    success_url = reverse_lazy("dashboard")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "A fruta foi Cadastrada")
        return super(FrutaView,self).form_valid(form)
    
class FrutaList(GroupRequiredMixin, ListView):
    group_required = [u'gerente', u'tecdealimentos']
    model = Fruta
    queryset = Fruta.objects.all()
    template_name = 'production/fruta_list.html'
    paginate_by = 5
    
class FrutaUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'gerente', u'tecdealimentos']
    model = Fruta
    fields = ['nome', 'preco', 'condicao']
    template_name = 'production/fruta_update.html'
    success_url = reverse_lazy("dashboard")
    
class CompraView(GroupRequiredMixin, View):
    group_required = [u'gerente', u'tecdealimentos']
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
   
class CompraList(GroupRequiredMixin, ListView):
    group_required = [u'gerente', u'tecdealimentos']
    model = Compra
    queryset = Compra.objects.all()
    template_name = 'production/compra_list.html'
    paginate_by = 5
    
# myapp/context_processors.py

def global_context(request):
    estoques = EstoqueFruta.objects.all()
    estoques_porcentagem = []
    
    for estoque in estoques:
        porcentagem = ((estoque.quantidade_atual / estoque.quantidade_max) *  100) if estoque.quantidade_max != 0 else 0
        estoques_porcentagem.append({
            'estoque': estoque,
            'porcentagem': porcentagem
        })
    
    return {
        'estoques': estoques_porcentagem
    }

    
class ProducaoView(GroupRequiredMixin, View):
    group_required = [u'gerente', u'gerdeproducao']
    form_class = ProducaoForm
    initial = {'key': 'value'}
    template_name = 'production/producao_register.html'

    def get(self, request):

        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form': self.form_class})
    
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'produção registrada')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})
    
class ProducaoList(GroupRequiredMixin, ListView):
    group_required = [u'gerente', u'gerdeproducao']
    model = Producao
    queryset = Producao.objects.all()
    template_name = 'production/producao_list.html'
    paginate_by = 5
    
class EstoquePolpaView(GroupRequiredMixin, ListView):
    group_required = [u'gerente', u'gerdeproducao']
    model = EstoquePolpa
    queryset = EstoquePolpa.objects.all()
    template_name = 'production/estoque_polpa_list.html'

def global_context_polpa_view(request):
    estoques_polpa = EstoquePolpa.objects.all()
    estoques_polpa_porcentagem = []
    
    for estoque_polpa in estoques_polpa:
        porcentagem_polpa = ((estoque_polpa.quantidade_atual / estoque_polpa.quantidade_max) *  100) if estoque_polpa.quantidade_max != 0 else 0
        estoques_polpa_porcentagem.append({
            'estoque_polpa': estoque_polpa,
            'porcentagem_polpa': porcentagem_polpa
        })
    
    return {
        'estoques_polpa': estoques_polpa_porcentagem
    }
    
class EntregaView(GroupRequiredMixin, View):
    group_required = u'gerente'
    form_class = EntregaForm
    initial = {'key': 'value'}
    template_name = 'production/entrega_register.html'

    def get(self, request):

        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form': self.form_class})
    
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Entrega Registrada')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})
    
class EntregaList(GroupRequiredMixin, ListView):
    group_required = [u'gerente', u'entregador']
    model = Entrega
    queryset = Entrega.objects.all()
    template_name = 'production/entrega_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        queryset = Entrega.objects.annotate(
            em_rota_first=Case(
                When(status=False, then=Value(1)),
                default=Value(0),
                output_field=BooleanField()
            )
        ).order_by('-em_rota_first', '-id')

        return queryset
    
class StatusEntrega(UpdateView):
    model = Entrega
    template_name = 'production/entrega_list.html'
    paginate_by = 5
    queryset = Entrega.objects.order_by('pk')
    
    def post(self, request, *args, **kwargs):
        entrega = self.get_object()
        entrega.status = True
        entrega.save()

        return JsonResponse({'message': 'Entrega confirmada com sucesso!'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)  # Adicione esta linha para imprimir o contexto no console do servidor
        return context

    success_url = reverse_lazy('dashboard')
        
    