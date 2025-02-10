import datetime
from Models.base_model import BaseModel

class Transacao(BaseModel):
    table_name = "Transacao"
    primary_key = "id_transacao"
    
    def __init__(self, id_transacao=None, id_carteira=None, id_tipo_transacao=None, valor=None, 
                 descricao=None, dt_hora=None):
        self.id_transacao = id_transacao
        self.id_carteira = id_carteira
        self.id_tipo_transacao = id_tipo_transacao
        self.valor = valor
        self.descricao = descricao
        self.dt_hora = dt_hora or datetime.datetime.now()
    
    def __str__(self):
        return (f"Transacao(id_transacao={self.id_transacao}, id_carteira={self.id_carteira}, "
                f"id_tipo_transacao={self.id_tipo_transacao}, valor={self.valor}, descricao={self.descricao}, "
                f"dt_hora={self.dt_hora})")