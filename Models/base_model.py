# Models/base_model.py
from Database.repository import insert, get, get_by, get_all, update, delete

class BaseModel:
    # Cada model derivada deve definir essas variáveis.
    table_name = None
    primary_key = None

    @classmethod
    def create(cls, **kwargs):
        """
        Insere um novo registro na tabela correspondente e retorna uma instância da classe.
        Essa implementação usa a função insert da repository.
        """
        if cls.table_name is None or cls.primary_key is None:
            raise NotImplementedError("Defina table_name e primary_key na sua model.")
        
        data = kwargs.copy()
        # Chama a função insert para inserir os dados e obter o novo id
        new_id = insert(cls.table_name, data)
        # Cria a instância passando os dados
        instance = cls(**kwargs)
        # Atribui o id gerado à instância
        setattr(instance, cls.primary_key, new_id)
        return instance

    @classmethod
    def get(cls, primary_key_value):
        """
        Recupera um registro da tabela baseado na chave primária.
        Retorna o registro bruto (tuple) ou None se não encontrado.
        Se desejar, cada model pode sobrescrever esse método para retornar uma instância.
        """
        if cls.table_name is None or cls.primary_key is None:
            raise NotImplementedError("Defina table_name e primary_key na sua model.")
        record = get(cls.table_name, primary_key_value, cls.primary_key)
        return record

    @classmethod
    def get_by(cls, column, value):
        """
        Recupera registros da tabela onde a coluna possui o valor especificado.
        Retorna uma lista de registros (tuplas).
        """
        if cls.table_name is None:
            raise NotImplementedError("Defina table_name na sua model.")
        records = get_by(cls.table_name, column, value)
        return records

    @classmethod
    def get_all(cls):
        """
        Recupera todos os registros da tabela.
        Retorna uma lista de registros (tuplas).
        """
        if cls.table_name is None:
            raise NotImplementedError("Defina table_name na sua model.")
        records = get_all(cls.table_name)
        return records

    def update(self, **kwargs):
        """
        Atualiza os atributos da instância e chama a função update da repository.
        Retorna a própria instância se bem-sucedido ou None caso contrário.
        """
        if self.__class__.table_name is None or self.__class__.primary_key is None:
            raise NotImplementedError("Defina table_name e primary_key na sua model.")
        pk_value = getattr(self, self.__class__.primary_key)
        # Atualiza os atributos locais
        for key, value in kwargs.items():
            setattr(self, key, value)
        success = update(self.__class__.table_name, pk_value, kwargs, self.__class__.primary_key)
        return self if success else None

    def delete(self):
        """
        Remove o registro correspondente à instância do banco de dados, usando a função delete.
        Retorna True se a operação for bem-sucedida, ou False caso contrário.
        """
        if self.__class__.table_name is None or self.__class__.primary_key is None:
            raise NotImplementedError("Defina table_name e primary_key na sua model.")
        pk_value = getattr(self, self.__class__.primary_key)
        return delete(self.__class__.table_name, pk_value, self.__class__.primary_key)

    @classmethod
    def generate_random(cls):
        raise NotImplementedError("Subclasses devem implementar generate_random")
