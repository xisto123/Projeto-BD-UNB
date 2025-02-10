from Models.base_model import BaseModel

class ResultadoPartidaEquipe(BaseModel):
    table_name = "Resultado_Partida_Equipe"
    primary_key = "id_resultado"
    
    def __init__(self, id_resultado=None, id_partida=None, id_equipe=None, gols_marcados=0, 
                 gols_sofridos=0, cartoes_amarelos=0, cartoes_vermelhos=0, escanteios=0, 
                 impedimentos=0, faltas_cometidas=0):
        self.id_resultado = id_resultado
        self.id_partida = id_partida
        self.id_equipe = id_equipe
        self.gols_marcados = gols_marcados
        self.gols_sofridos = gols_sofridos
        self.cartoes_amarelos = cartoes_amarelos
        self.cartoes_vermelhos = cartoes_vermelhos
        self.escanteios = escanteios
        self.impedimentos = impedimentos
        self.faltas_cometidas = faltas_cometidas
    
    def __str__(self):
        return (f"ResultadoPartidaEquipe(id_resultado={self.id_resultado}, id_partida={self.id_partida}, "
                f"id_equipe={self.id_equipe}, gols_marcados={self.gols_marcados}, "
                f"gols_sofridos={self.gols_sofridos}, cartoes_amarelos={self.cartoes_amarelos}, "
                f"cartoes_vermelhos={self.cartoes_vermelhos}, escanteios={self.escanteios}, "
                f"impedimentos={self.impedimentos}, faltas_cometidas={self.faltas_cometidas})")