from django.urls import path
from .views import *

app_name = "production"

urlpatterns = [
    path('fruta_register/', FrutaView.as_view(), name="fruta_register"),
    path('list_fruta/', FrutaList.as_view(), name="list_fruta"),
    path('update_fruta/<int:pk>', FrutaUpdate.as_view(), name="update_fruta"),
    
    ################################  compra  #################################
    
    path('compra_register/', CompraView.as_view(), name="compra_register"),
    path('list_compra/', CompraList.as_view(), name="list_compra"),
    
    path('list_estoque/', EstoqueView.as_view(), name="list_estoque"),
    
    ################################  Produção  #################################
    
    path('producao_register/', ProducaoView.as_view(), name="producao_register"),
    path('list_producao/', ProducaoList.as_view(), name="list_producao"),
    
    path('list_estoque_polpa/', EstoquePolpaView.as_view(), name="list_estoque_polpa"),
]

