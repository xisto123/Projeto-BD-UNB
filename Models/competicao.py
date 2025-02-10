from Models.base_model import BaseModel

class Competicao(BaseModel):
    table_name = "Competicao"
    primary_key = "id_competicao"
    
    def __init__(self, id_competicao=None, nome=None, organizacao=None, id_tipo_competicao=None):
        self.id_competicao = id_competicao
        self.nome = nome
        self.organizacao = organizacao
        self.id_tipo_competicao = id_tipo_competicao
    
    def __str__(self):
        return (f"Competicao(id_competicao={self.id_competicao}, nome={self.nome}, "
                f"organizacao={self.organizacao}, id_tipo_competicao={self.id_tipo_competicao})")