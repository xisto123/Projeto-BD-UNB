from Models.base_model import BaseModel

class MercadoAposta(BaseModel):
    table_name = "Mercado_Aposta"
    primary_key = "id_mercado"
    
    def __init__(self, id_mercado=None, tipo_aposta=None, descricao=None):
        self.id_mercado = id_mercado
        self.tipo_aposta = tipo_aposta
        self.descricao = descricao
    
    def __str__(self):
        return (f"MercadoAposta(id_mercado={self.id_mercado}, tipo_aposta={self.tipo_aposta}, "
                f"descricao={self.descricao})")