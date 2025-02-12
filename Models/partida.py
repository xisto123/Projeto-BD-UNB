import datetime
from Models.base_model import BaseModel

class Partida(BaseModel):
    table_name = "Partida"
    primary_key = "id_partida"
    
    def __init__(self, id_partida=None, id_competicao=None, id_time_mandante=None, 
                 id_time_visitante=None, estadio=None, dt_hora_inicio=None, 
                 id_tipo_partida=None, id_status_partida=None):
        self.id_partida = id_partida
        self.id_competicao = id_competicao
        self.id_time_mandante = id_time_mandante
        self.id_time_visitante = id_time_visitante
        self.estadio = estadio
        self.dt_hora_inicio = dt_hora_inicio
        self.id_tipo_partida = id_tipo_partida
        self.id_status_partida = id_status_partida
    
    def __str__(self):
        return (f"Partida(id_partida={self.id_partida}, id_competicao={self.id_competicao}, "
                f"id_time_mandante={self.id_time_mandante}, id_time_visitante={self.id_time_visitante}, "
                f"estadio={self.estadio}, dt_hora_inicio={self.dt_hora_inicio}, "
                f"id_tipo_partida={self.id_tipo_partida}, id_status_partida={self.id_status_partida})")
