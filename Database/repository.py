# Database/repository.py

from .connection import get_connection
from Services.global_data import TRANSACTION_CONN  # Importa diretamente o TRANSACTION_CONN

# Mapeamento do nome da tabela para o nome da coluna da chave primária
PK_MAP = {
    "Aposta": "id_aposta",
    "Arquivo": "id_arquivo",
    "Carteira": "id_carteira",
    "Competicao": "id_competicao",
    "Equipe": "id_equipe",
    "Login": "id_login",
    "Mercado_Aposta": "id_mercado",
    "Notificacao": "id_notificacao",
    "Notificacao_Lote": "id_notificacao_lote",
    "Odd": "id_odd",
    "Partida": "id_partida",
    "Resultado_Aposta": "id_resultado_aposta",
    "Resultado_Partida_Equipe": "id_resultado",
    "Status_Carteira": "id_status_carteira",
    "Status_Resultado_Aposta": "id_status_resultado_aposta",
    "Tipo_Competicao": "id_tipo_competicao",
    "Tipo_Notificacao": "id_tipo_notificacao",
    "Tipo_Partida": "id_tipo_partida",
    "Tipo_Transacao": "id_tipo_transacao",
    "Tipo_Usuario": "id_tipo_usuario",
    "Transacao": "id_transacao",
    "Usuario": "id_usuario"
}

def _get_pk_column(table: str, primary_key_column: str = None) -> str:
    return primary_key_column if primary_key_column else PK_MAP.get(table, "id")

def _obter_conexao(conn):
    """
    Retorna a conexão a ser usada. Se um objeto de conexão for passado no parâmetro conn,
    ele será utilizado. Caso contrário, se TRANSACTION_CONN estiver definido,
    esse será utilizado. Se nenhum estiver definido, abre uma nova conexão.
    
    Retorna uma tupla: (conn, local_conn)
    - conn: objeto de conexão.
    - local_conn: booleano indicando se a conexão foi aberta localmente (True) ou não.
    """
    if conn is not None:
        return conn, False
    if TRANSACTION_CONN is not None:
        return TRANSACTION_CONN, False
    new_conn = get_connection()
    return new_conn, True

def insert(table, data: dict, conn=None):
    """
    Insere um registro na tabela especificada e retorna o ID gerado.
    """
    conn, local_conn = _obter_conexao(conn)
    cursor = conn.cursor()
    
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    primary_key = _get_pk_column(table)
    
    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders}) RETURNING {primary_key};"
    values = list(data.values())
    
    cursor.execute(query, values)
    new_id = cursor.fetchone()[0]
    if local_conn:
        conn.commit()
        cursor.close()
        conn.close()
    else:
        cursor.close()
    return new_id

def get(table, primary_key_value, primary_key_column=None, conn=None):
    """
    Recupera um registro da tabela baseado na chave primária.
    """
    conn, local_conn = _obter_conexao(conn)
    cursor = conn.cursor()
    
    pk = _get_pk_column(table, primary_key_column)
    query = f"SELECT * FROM {table} WHERE {pk} = %s;"
    
    cursor.execute(query, (primary_key_value,))
    record = cursor.fetchone()
    cursor.close()
    if local_conn:
        conn.close()
    return record

def get_by(table, column, value, conn=None):
    """
    Recupera registros da tabela onde a coluna tem determinado valor.
    """
    conn, local_conn = _obter_conexao(conn)
    cursor = conn.cursor()
    
    query = f"SELECT * FROM {table} WHERE {column} = %s;"
    cursor.execute(query, (value,))
    records = cursor.fetchall()
    
    cursor.close()
    if local_conn:
        conn.close()
    return records

def get_all(table_name, conn=None):
    """
    Recupera todos os registros da tabela especificada.
    Retorna uma lista de registros (tuplas).
    """
    conn, local_conn = _obter_conexao(conn)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()
    cursor.close()
    if local_conn:
        conn.close()
    return records

def update(table, primary_key_value, data: dict, primary_key_column=None, conn=None):
    """
    Atualiza um registro na tabela especificada.
    """
    conn, local_conn = _obter_conexao(conn)
    cursor = conn.cursor()
    
    pk = _get_pk_column(table, primary_key_column)
    set_clause = ', '.join([f"{col} = %s" for col in data.keys()])
    values = list(data.values())
    values.append(primary_key_value)
    
    query = f"UPDATE {table} SET {set_clause} WHERE {pk} = %s;"
    cursor.execute(query, values)
    if local_conn:
        conn.commit()
        cursor.close()
        conn.close()
    else:
        cursor.close()
    return True

def delete(table, primary_key_value, primary_key_column=None, conn=None):
    """
    Exclui um registro da tabela especificada.
    """
    conn, local_conn = _obter_conexao(conn)
    cursor = conn.cursor()
    
    pk = _get_pk_column(table, primary_key_column)
    query = f"DELETE FROM {table} WHERE {pk} = %s;"
    
    cursor.execute(query, (primary_key_value,))
    if local_conn:
        conn.commit()
        cursor.close()
        conn.close()
    else:
        cursor.close()
    return True

def call_sp_cadastrar_usuario_completo(p_nome, p_cpf, p_email, p_senha, p_id_tipo_usuario, p_dt_nascimento, foto_info):
    """
    Chama a procedure armazenada cadastrar_usuario_completo que realiza o cadastro completo do usuário.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        if foto_info is None:
            foto_data = None
            foto_nome = None
            foto_mime = None
            foto_size = None
        else:
            foto_data = foto_info.get("binary_data")
            foto_nome = foto_info.get("file_name")
            foto_mime = foto_info.get("mime_type")
            foto_size = foto_info.get("file_size_mb")
        
        cursor.execute(
            "CALL cadastrar_usuario_completo(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [
                p_nome,
                p_cpf,
                p_email,
                p_senha,
                p_id_tipo_usuario,
                p_dt_nascimento,
                foto_data,
                foto_nome,
                foto_mime,
                foto_size
            ]
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Erro ao cadastrar usuário completo via procedure:", e)
        return False

def call_sp_encerrar_partida(p_id_partida, p_gols_mandante, p_gols_visitante,
                             p_cartoes_amarelos_mandante, p_cartoes_amarelos_visitante,
                             p_cartoes_vermelhos_mandante, p_cartoes_vermelhos_visitante,
                             p_escanteios_mandante, p_escanteios_visitante,
                             p_impedimentos_mandante, p_impedimentos_visitante,
                             p_faltas_mandante, p_faltas_visitante, conn=None):
    try:
        conn = conn if conn is not None else get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "CALL encerrar_partida(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [
                p_id_partida,
                p_gols_mandante,
                p_gols_visitante,
                p_cartoes_amarelos_mandante,
                p_cartoes_amarelos_visitante,
                p_cartoes_vermelhos_mandante,
                p_cartoes_vermelhos_visitante,
                p_escanteios_mandante,
                p_escanteios_visitante,
                p_impedimentos_mandante,
                p_impedimentos_visitante,
                p_faltas_mandante,
                p_faltas_visitante
            ]
        )
        conn.commit()
        cursor.close()
        if conn is None:
            conn.close()
        return True
    except Exception as e:
        print("Erro ao executar a procedure encerrar_partida:", e)
        return False

def fetch_apostas_em_andamento():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM vw_apostas_em_andamento;"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def fetch_detalhes_times():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM vw_detalhes_times;"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
