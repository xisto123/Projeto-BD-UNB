import datetime
from Models.base_model import BaseModel

class ResultadoAposta(BaseModel):
    table_name = "Resultado_Aposta"
    primary_key = "id_resultado_aposta"
    
    def __init__(self, id_resultado_aposta=None, id_aposta=None, valor_recebido=0.00, 
                 id_status_resultado_aposta=None, dt_hora_registro=None):
        self.id_resultado_aposta = id_resultado_aposta
        self.id_aposta = id_aposta
        self.valor_recebido = valor_recebido
        self.id_status_resultado_aposta = id_status_resultado_aposta
        self.dt_hora_registro = dt_hora_registro or datetime.datetime.now()
    
    def __str__(self):
        return (f"ResultadoAposta(id_resultado_aposta={self.id_resultado_aposta}, id_aposta={self.id_aposta}, "
                f"valor_recebido={self.valor_recebido}, id_status_resultado_aposta={self.id_status_resultado_aposta}, "
                f"dt_hora_registro={self.dt_hora_registro})")