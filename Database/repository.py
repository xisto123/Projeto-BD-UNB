# Database/repository.py

from .connection import get_connection

def insert(table, data: dict):
    """
    Insere um registro na tabela especificada e retorna o ID gerado.
    Para definir qual é o campo chave primária, usamos um mapeamento simples.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    
    # Mapeamento do nome da tabela para o nome da coluna da chave primária
    pk_map = {
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
    
    primary_key = pk_map.get(table, "id")
    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders}) RETURNING {primary_key};"
    values = list(data.values())
    cursor.execute(query, values)
    new_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return new_id
