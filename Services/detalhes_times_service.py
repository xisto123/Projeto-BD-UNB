from Database.repository import fetch_detalhes_times

class DetalhesTimesService:
    def __init__(self):
        # Armazena a função, não o resultado da chamada
        self.repository = fetch_detalhes_times

    def get_detalhes_times(self):
        # Chama a função para obter os dados
        return self.repository()