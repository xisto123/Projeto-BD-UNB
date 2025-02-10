# Models/notificacao.py

import datetime
from Models.base_model import BaseModel

class Notificacao(BaseModel):
    table_name = "Notificacao"
    primary_key = "id_notificacao"
    
    def __init__(self, id_notificacao=None, id_usuario=None, id_tipo_notificacao=None, 
                 titulo=None, conteudo=None, status_leitura=False, dt_hora_envio=None):
        self.id_notificacao = id_notificacao
        self.id_usuario = id_usuario
        self.id_tipo_notificacao = id_tipo_notificacao
        self.titulo = titulo
        self.conteudo = conteudo
        self.status_leitura = status_leitura
        self.dt_hora_envio = dt_hora_envio or datetime.datetime.now()
    
    def __str__(self):
        return (f"Notificacao(id_notificacao={self.id_notificacao}, id_usuario={self.id_usuario}, "
                f"id_tipo_notificacao={self.id_tipo_notificacao}, titulo={self.titulo}, conteudo={self.conteudo}, "
                f"status_leitura={self.status_leitura}, dt_hora_envio={self.dt_hora_envio})")
