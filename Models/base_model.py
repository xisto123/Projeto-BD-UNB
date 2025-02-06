# Models/base_model.py

class BaseModel:
    @classmethod
    def create(cls, **kwargs):
        """
        Método base para criação.
        Em cada Model você poderá sobrescrever esse método para integrar
        com a função de inserção do repositório.
        """
        instance = cls(**kwargs)
        return instance

    @classmethod
    def get(cls, primary_key):
        # Implementação da consulta pelo ID
        raise NotImplementedError

    @classmethod
    def get_by(cls, column, value):
        # Implementação da consulta filtrada por coluna e valor
        raise NotImplementedError

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        # Aqui você chamaria a função de atualização no BD
        return self

    def delete(self):
        # Aqui você chamaria a função de deleção no BD
        raise NotImplementedError

    @classmethod
    def generate_random(cls):
        raise NotImplementedError("Subclasses devem implementar generate_random")
