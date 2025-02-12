# Models/base_model.py
from Database.repository import insert, get, get_by, get_all, update, delete

class BaseModel:
    # Cada model derivada deve definir essas variáveis.
    table_name = None
    primary_key = None

    @classmethod
    def create(cls, conn=None, **kwargs):
        """
        Insere um novo registro na tabela correspondente e retorna uma instância da classe.
        Aceita um parâmetro opcional 'conn' que, se fornecido, será utilizado para as operações.
        """
        if cls.table_name is None or cls.primary_key is None:
            raise NotImplementedError("Defina table_name e primary_key na sua model.")
        
        # Remove 'conn' de kwargs para não enviá-lo como dado
        kwargs.pop("conn", None)
        data = kwargs.copy()
        new_id = insert(cls.table_name, data, conn=conn)
        instance = cls(**kwargs)
        setattr(instance, cls.primary_key, new_id)
        return instance

    @classmethod
    def get(cls, primary_key_value, conn=None):
        """
        Recupera um registro da tabela baseado na chave primária.
        Retorna o registro bruto (tuple) ou None se não encontrado.
        """
        if cls.table_name is None or cls.primary_key is None:
            raise NotImplementedError("Defina table_name e primary_key na sua model.")
        record = get(cls.table_name, primary_key_value, cls.primary_key, conn=conn)
        return record

    @classmethod
    def get_by(cls, column, value, conn=None):
        """
        Recupera registros da tabela onde a coluna possui o valor especificado.
        Retorna uma lista de registros (tuplas).
        """
        if cls.table_name is None:
            raise NotImplementedError("Defina table_name na sua model.")
        records = get_by(cls.table_name, column, value, conn=conn)
        return records

    @classmethod
    def get_all(cls, conn=None):
        """
        Recupera todos os registros da tabela.
        Retorna uma lista de registros (tuplas).
        """
        if cls.table_name is None:
            raise NotImplementedError("Defina table_name na sua model.")
        records = get_all(cls.table_name, conn=conn)
        return records

    def update(self, conn=None, **kwargs):
        """
        Atualiza os atributos da instância e chama a função update da repository.
        Retorna a própria instância se bem-sucedido ou None caso contrário.
        """
        if self.__class__.table_name is None or self.__class__.primary_key is None:
            raise NotImplementedError("Defina table_name e primary_key na sua model.")
        pk_value = getattr(self, self.__class__.primary_key)
        for key, value in kwargs.items():
            setattr(self, key, value)
        success = update(self.__class__.table_name, pk_value, kwargs, self.__class__.primary_key, conn=conn)
        return self if success else None

    @classmethod
    def update_by_pk(cls, pk_value, conn=None, **kwargs):
        """
        Atualiza o registro na tabela baseado na chave primária e retorna a instância atualizada.
        """
        success = update(cls.table_name, pk_value, kwargs, cls.primary_key, conn=conn)
        if success:
            # Se houver um método get_by_id, você pode utilizá-lo; caso contrário, use get e converta o registro conforme sua necessidade.
            return cls.get(pk_value, conn=conn)
        return None

    def delete(self, conn=None):
        """
        Remove o registro correspondente à instância do banco de dados.
        Retorna True se a operação for bem-sucedida, ou False caso contrário.
        """
        if self.__class__.table_name is None or self.__class__.primary_key is None:
            raise NotImplementedError("Defina table_name e primary_key na sua model.")
        pk_value = getattr(self, self.__class__.primary_key)
        return delete(self.__class__.table_name, pk_value, self.__class__.primary_key, conn=conn)
    
    @classmethod
    def delete_by_pk(cls, pk_value, conn=None):
        """
        Exclui um registro diretamente pela chave primária.
        Retorna True se a operação for bem-sucedida ou False caso contrário.
        """
        if cls.table_name is None or cls.primary_key is None:
            raise NotImplementedError("Defina table_name e primary_key na sua model.")
        return delete(cls.table_name, pk_value, cls.primary_key, conn=conn)

    @classmethod
    def generate_random(cls):
        raise NotImplementedError("Subclasses devem implementar generate_random")
