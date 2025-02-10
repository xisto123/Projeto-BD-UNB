from Models.base_model import BaseModel

class Equipe(BaseModel):
    table_name = "Equipe"
    primary_key = "id_equipe"
    
    def __init__(self, id_equipe=None, nome=None, pais=None):
        self.id_equipe = id_equipe
        self.nome = nome
        self.pais = pais
    
    def __str__(self):
        return (f"Equipe(id_equipe={self.id_equipe}, nome={self.nome}, pais={self.pais})")