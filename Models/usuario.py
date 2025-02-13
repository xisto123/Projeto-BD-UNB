# Models/usuario.py

import datetime
import random
import string
from Models.base_model import BaseModel
from Database.repository import insert, get_by, get, update, delete

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

    nomes_comuns = ["Maria", "Ana", "Francisca", "Antônio", "João", "Carlos", "Paulo", "Pedro", "Lucas", "Luiz",
        "Marcos", "José", "Francisco", "Raimundo", "Sebastião", "Manoel", "Joaquim", "Domingos", "Jorge", "Ricardo",
        "Daniel", "Rafael", "Gabriel", "Felipe", "Bruno", "Gustavo", "Mateus", "Rodrigo", "Thiago", "Eduardo"]
    
    sobrenomes_comuns = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Almeida", "Costa", "Gomes", "Martins",
        "Araújo", "Melo", "Barbosa", "Ribeiro", "Alves", "Pereira", "Lima", "Carvalho", "Pinto", "Cavalcanti",
        "Monteiro", "Moura", "Rocha", "Dias", "Nunes", "Vieira", "Cardoso", "Leite", "Cunha", "Campos"]

    @classmethod
    def get_by_cpf(cls, cpf):
        """
        Consulta a tabela de Usuario buscando pelo CPF.
        """
        records = get_by("Usuario", "cpf", cpf)
        if records and len(records) > 0:
            record = records[0]

            return cls(
                id_usuario=record[0],
                nome=record[1],
                cpf=record[2],
                email=record[3],
                senha=record[4],
                id_tipo_usuario=record[5],
                status=record[6],
                dt_nascimento=record[7],
                dt_hora_registro=record[8]
            )
        return None
    
    @classmethod
    def get_by_id(cls, id_usuario):
        """
        Consulta a tabela de Usuario buscando pelo Id.
        """
        record = get("Usuario", id_usuario)
        if record:

            return cls(
                id_usuario=record[0],
                nome=record[1],
                cpf=record[2],
                email=record[3],
                senha=record[4],
                id_tipo_usuario=record[5],
                status=record[6],
                dt_nascimento=record[7],
                dt_hora_registro=record[8]
            )
        return None

    @classmethod
    def authenticate(cls, cpf, senha):
        """
        Autentica o usuário pelo CPF e senha (comparação literal).
        """
        usuario = cls.get_by_cpf(cpf)
        if usuario and usuario.senha == senha:
            return usuario
        return None

    @classmethod
    def generate_random(cls):       
        nome = f"{random.choice(cls.nomes_comuns)} {random.choice(cls.sobrenomes_comuns)}"
        cpf = ''.join(random.choices(string.digits, k=11))
        email = f"user{random.randint(1,1000)}@example.com"
        senha = "senha123"
        id_tipo_usuario = random.randint(1, 5)
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
            dt_nascimento=dt_nascimento
        )
    
    @classmethod
    def editar(cls, id_usuario, **kwargs):
        """
        Edita os dados de um usuário no banco de dados utilizando a repository.
        Os campos que podem ser atualizados são: nome, cpf, email, senha, id_tipo_usuario e dt_nascimento.
        Retorna a instância atualizada se a operação for bem-sucedida, ou None caso contrário.
        """
        # Monta o dicionário com os campos a serem atualizados
        data = {}
        campos = ["nome", "cpf", "email", "senha", "id_tipo_usuario", "dt_nascimento"]
        for campo in campos:
            if campo in kwargs:
                data[campo] = kwargs[campo]
        success = update("Usuario", id_usuario, data)
        if success:
            return cls.get_by_id(id_usuario)
        return None

    @classmethod
    def excluir(cls, id_usuario):
        """
        Exclui um usuário do banco de dados utilizando a repository.
        Retorna True se a exclusão for bem-sucedida, ou False caso contrário.
        """
        return delete("Usuario", id_usuario)
