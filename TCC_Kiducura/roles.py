from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {"register":True, 'users':True, 'update_user':True, 'detail_user':True}
    
class Entregador(AbstractUserRole):
    available_permissions = {'list_entrega': True, 'status_entrega': True}
    
class TecAlimentos(AbstractUserRole):
    available_permissions = {'fruta_register': True, 'list_fruta': True, 'update_fruta': True, 'compra_register': True, 'list_compra' : True , 'list_estoque': True, 'produtor_register': True, 'produtor_list':True, 'update_produtor':True, 'detail_produtor': True}
    
class GerProducao(AbstractUserRole):
    available_permissions = {'producao_register': True, 'list_producao': True, 'list_estoque_polpa':True, 'list_estoque':True}