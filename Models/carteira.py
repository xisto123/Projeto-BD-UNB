import datetime
from decimal import Decimal
from Models.base_model import BaseModel

class Carteira(BaseModel):
    table_name = "Carteira"
    primary_key = "id_carteira"
    
    def __init__(self, id_carteira=None, id_usuario=None, tipo='principal', saldo=0.00, 
                 id_status_carteira=None, dt_hora_registro=None, dt_hora_atualizacao=None):
        self.id_carteira = id_carteira
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.saldo = saldo
        self.id_status_carteira = id_status_carteira
        self.dt_hora_registro = dt_hora_registro or datetime.datetime.now()
        self.dt_hora_atualizacao = dt_hora_atualizacao or datetime.datetime.now()
    
    def __str__(self):
        return (f"Carteira(id_carteira={self.id_carteira}, id_usuario={self.id_usuario}, "
                f"tipo={self.tipo}, saldo={self.saldo}, id_status_carteira={self.id_status_carteira}, "
                f"dt_hora_registro={self.dt_hora_registro}, dt_hora_atualizacao={self.dt_hora_atualizacao})")
    
    @classmethod
    def get_saldo_usuario(cls, id_usuario):
        carteira = cls.get_by("id_usuario", id_usuario)
        if carteira:
            # Retorna o saldo assumindo que esteja na posição 3 da tupla.
            return carteira[0][3]
        return None
    
    @classmethod
    def verifica_saldo(cls, id_usuario, valor_aposta=0):
        saldo = cls.get_saldo_usuario(id_usuario)
        try:
            aposta = valor_aposta if isinstance(valor_aposta, Decimal) else Decimal(valor_aposta)
        except Exception:
            return False

        if saldo is not None:
            return saldo >= aposta
        return False