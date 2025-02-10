from Database.repository import call_sp_cadastrar_usuario_completo
from Enums.tipos_apoio import TipoUsuario
import datetime
import re

def cadastrar_usuario_completo(nome, cpf, email, senha, tipo_usuario_label, dt_nascimento_str, foto_info):
    """
    Recebe os dados do usuário e os dados da foto (foto_info pode ser None).
    Realiza as conversões necessárias e chama a camada de persistência para cadastrar o usuário completo.
    
    Parâmetros:
      - nome, cpf, email, senha: strings com os dados do usuário.
      - tipo_usuario_label: o valor do combobox.
      - dt_nascimento_str: data no formato string (YYYY-MM-DD).
      - foto_info: dicionário com os metadados da foto ou None.
    
    Retorna True se o cadastro for realizado com sucesso, False caso contrário.
    """
    # Validar o formato do email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError("Formato de email inválido.")
    
    # Validar o número de caracteres do CPF
    if len(cpf) != 11:
        raise ValueError("O CPF deve conter 11 caracteres.")
    
    # Converter a data de nascimento
    try:
        dt_nascimento = datetime.datetime.strptime(dt_nascimento_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Data de nascimento inválida. Use o formato YYYY-MM-DD.")
    
    # Converter o label do tipo de usuário para seu valor numérico
    tipo_usuario_map = {tipo.name: tipo.value for tipo in TipoUsuario}
    id_tipo_usuario = tipo_usuario_map.get(tipo_usuario_label)
    if id_tipo_usuario is None:
        raise ValueError("Tipo de usuário inválido.")
    
    # Chama a função que invoca a procedure na camada repository
    sucesso = call_sp_cadastrar_usuario_completo(
        p_nome=nome,
        p_cpf=cpf,
        p_email=email,
        p_senha=senha,
        p_id_tipo_usuario=id_tipo_usuario,
        p_dt_nascimento=dt_nascimento,
        foto_info=foto_info
    )
    
    return sucesso
