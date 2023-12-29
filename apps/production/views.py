from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from .models import Fruta
from .form import FrutaForm

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