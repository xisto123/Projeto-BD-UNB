import datetime
from Models.base_model import BaseModel

class Odd(BaseModel):
    table_name = "Odd"
    primary_key = "id_odd"
    
    def __init__(self, id_odd=None, id_partida=None, id_mercado=None, valor=None, 
                 descricao=None, dt_hora_criacao=None, dt_hora_atualizacao=None):
        self.id_odd = id_odd
        self.id_partida = id_partida
        self.id_mercado = id_mercado
        self.valor = valor
        self.descricao = descricao
        self.dt_hora_criacao = dt_hora_criacao or datetime.datetime.now()
        self.dt_hora_atualizacao = dt_hora_atualizacao or datetime.datetime.now()
    
    def __str__(self):
        return (f"Odd(id_odd={self.id_odd}, id_partida={self.id_partida}, id_mercado={self.id_mercado}, "
                f"valor={self.valor}, descricao={self.descricao}, dt_hora_criacao={self.dt_hora_criacao}, "
                f"dt_hora_atualizacao={self.dt_hora_atualizacao})")