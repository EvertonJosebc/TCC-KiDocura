from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {"register":True, 'users':True, 'update_user':True, 'detail_user':True, 'cliente_register':True, 'list_cliente':True, 'update_cliente':True, 'detail_cliente':True}
    
class Entregador(AbstractUserRole):
    available_permissions = {'list_entrega': True, 'status_entrega': True}
    
class Tecdealimentos(AbstractUserRole):
    available_permissions = {'fruta_register': True, 'list_fruta': True, 'update_fruta': True, 'compra_register': True, 'list_compra' : True , 'list_estoque': True, 'produtor_register': True, 'produtor_list':True, 'update_produtor':True, 'detail_produtor': True}
    
class Gerdeproducao(AbstractUserRole):
    available_permissions = {'producao_register': True, 'list_producao': True, 'list_estoque_polpa':True, 'list_estoque':True, 'compra_register': True, 'list_compra' : True , 'produtor_register': True, 'produtor_list':True, 'update_produtor':True, 'detail_produtor': True}
    
class Auxdeproducao(AbstractUserRole):
    available_permissions = {'producao_register': True, 'list_producao': True, 'list_estoque_polpa':True, 'list_estoque':True, 'compra_register': True, 'list_compra' : True}