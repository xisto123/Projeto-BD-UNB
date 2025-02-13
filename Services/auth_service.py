# Services/auth_service.py

from Models.usuario import Usuario
from Models.login import Login
import Services.global_data as global_data

def login(cpf, senha):
    """ Realiza o login do usuário e registra a tentativa no banco """
    try:
        usuario = Usuario.authenticate(cpf, senha)
        if usuario:
            sucesso = True

            global_data.usuario_id = usuario.id_usuario
            global_data.usuario_nome = usuario.nome
            global_data.usuario_tipo = usuario.id_tipo_usuario

            print("Login realizado com sucesso!")
        else:
            sucesso = False
            print("CPF ou senha incorretos.")

        # Registrar a tentativa de login usando o método de criação da Model Login
        data = {
            "id_usuario": usuario.id_usuario if usuario else None,
            "endereco_ip": Login.get_local_ip(),
            "sucesso": sucesso,
        }

        Login.create(**data)
        
        return sucesso

    except Exception as e:
        print(f"Erro no processo de login: {e}")
        return False
