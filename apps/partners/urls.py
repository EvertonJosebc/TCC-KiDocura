from django.urls import path
from .views import *

app_name = "partners"

urlpatterns = [
    path('cliente_register/', ClienteView.as_view(), name="cliente_register"),
    path('list_cliente/', ClienteList.as_view(), name="list_cliente"),
    path('update_cliente/<int:pk>', ClienteUpdate.as_view(), name="update_cliente"),
    path('detail_cliente/<int:pk>', ClienteDetail.as_view(), name="detail_cliente"),
    
    path('produtor_register/', ProdutorView.as_view(), name="produtor_register"),
    path('list_produtor/', ProdutorList.as_view(), name="list_produtor"),
    path('update_produtor/<int:pk>', ProdutorUpdate.as_view(), name="update_produtor"),
    path('detail_produtor/<int:pk>', ProdutorDetail.as_view(), name="detail_produtor"),
]