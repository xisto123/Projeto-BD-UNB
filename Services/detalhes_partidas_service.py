from Database.repository import fetch_apostas_em_andamento

class DetalhesPartidasService:
    def __init__(self):
        # Armazena a função, não o resultado da chamada
        self.repository = fetch_apostas_em_andamento

    def get_apostas_em_andamento(self):
        # Chama a função para obter os dados
        return self.repository()