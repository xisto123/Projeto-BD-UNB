import datetime
from Models.base_model import BaseModel

class Aposta(BaseModel):
    table_name = "Aposta"
    primary_key = "id_aposta"
    
    def __init__(self, id_aposta=None, id_usuario=None, id_odd=None, valor=None, 
                 resultado=None, status='ativa', dt_hora=None):
        self.id_aposta = id_aposta
        self.id_usuario = id_usuario
        self.id_odd = id_odd
        self.valor = valor
        self.resultado = resultado
        self.status = status
        self.dt_hora = dt_hora or datetime.datetime.now()
    
    def __str__(self):
        return (f"Aposta(id_aposta={self.id_aposta}, id_usuario={self.id_usuario}, "
                f"id_odd={self.id_odd}, valor={self.valor}, resultado={self.resultado}, "
                f"status={self.status}, dt_hora={self.dt_hora})")