# Models/usuario.py

import datetime
import random
import string
from Models.base_model import BaseModel
from Database.repository import insert

class Usuario(BaseModel):
    def __init__(self, id_usuario=None, nome=None, cpf=None, email=None, senha=None,
                 id_tipo_usuario=None, status="ativo", dt_nascimento=None, dt_hora_registro=None):
        self.id_usuario = id_usuario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.id_tipo_usuario = id_tipo_usuario
        self.status = status
        self.dt_nascimento = dt_nascimento
        self.dt_hora_registro = dt_hora_registro or datetime.datetime.now()

    def __str__(self):
        return (f"Usuario(id_usuario={self.id_usuario}, nome={self.nome}, cpf={self.cpf},\n"
                f"email={self.email}, senha={self.senha}, id_tipo_usuario={self.id_tipo_usuario},\n"
                f"status={self.status}, dt_nascimento={self.dt_nascimento},\n"
                f"dt_hora_registro={self.dt_hora_registro})")

    @classmethod
    def create(cls, **kwargs):
        """
        Insere um novo registro no banco de dados e retorna uma instância da classe.
        """
        # Prepara os dados para inserção (ajuste os nomes dos campos conforme sua tabela)
        data = {
            "nome": kwargs.get("nome"),
            "cpf": kwargs.get("cpf"),
            "email": kwargs.get("email"),
            "senha": kwargs.get("senha"),
            "id_tipo_usuario": kwargs.get("id_tipo_usuario"),
            "status": kwargs.get("status", "ativo"),
            "dt_nascimento": kwargs.get("dt_nascimento")
            # dt_hora_registro é definido automaticamente no BD ou aqui se preferir
        }
        # Chama a função de inserção do repositório
        new_id = insert("Usuario", data)
        return cls(id_usuario=new_id, **kwargs)

    @classmethod
    def generate_random(cls):
        nome = ''.join(random.choices(string.ascii_letters, k=10))
        cpf = ''.join(random.choices(string.digits, k=11))
        email = f"user{random.randint(1,1000)}@example.com"
        senha = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        id_tipo_usuario = random.randint(1, 3)
        status = random.choice(["ativo", "inativo"])
        start_date = datetime.date(1950, 1, 1)
        end_date = datetime.date(2000, 12, 31)
        delta = (end_date - start_date).days
        dt_nascimento = start_date + datetime.timedelta(days=random.randint(0, delta))

        return cls(
            nome=nome,
            cpf=cpf,
            email=email,
            senha=senha,
            id_tipo_usuario=id_tipo_usuario,
            status=status,
            dt_nascimento=dt_nascimento
        )
