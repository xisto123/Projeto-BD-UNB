import datetime
from Models.base_model import BaseModel

class Arquivo(BaseModel):
    table_name = "Arquivo"
    primary_key = "id_arquivo"
    
    def __init__(self, id_arquivo=None, id_usuario=None, nome=None, descricao=None, 
                 mime_type=None, size_mb=None, binary_data=None, dt_hora_upload=None):
        self.id_arquivo = id_arquivo
        self.id_usuario = id_usuario
        self.nome = nome
        self.descricao = descricao
        self.mime_type = mime_type
        self.size_mb = size_mb
        self.binary_data = binary_data
        self.dt_hora_upload = dt_hora_upload or datetime.datetime.now()
    
    def __str__(self):
        return (f"Arquivo(id_arquivo={self.id_arquivo}, id_usuario={self.id_usuario}, "
                f"nome={self.nome}, descricao={self.descricao}, mime_type={self.mime_type}, "
                f"size_mb={self.size_mb}, dt_hora_upload={self.dt_hora_upload})")