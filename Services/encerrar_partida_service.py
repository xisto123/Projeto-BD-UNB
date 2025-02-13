# Services/encerrar_partida_service.py

from Database.repository import call_sp_encerrar_partida

def encerrar_partida(
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
):
    """
    Executa a procedure 'encerrar_partida' no banco de dados, que encerra uma partida
    e registra os resultados (gols, cartões, escanteios, impedimentos e faltas) para os dois times.
    
    Valida se os parâmetros são inteiros não negativos e chama a função na repository.
    
    Retorna True se a procedure for executada com sucesso; caso contrário, lança exceção.
    """
    # Lista dos parâmetros e seus nomes para validação
    params = [
        p_id_partida, p_gols_mandante, p_gols_visitante,
        p_cartoes_amarelos_mandante, p_cartoes_amarelos_visitante,
        p_cartoes_vermelhos_mandante, p_cartoes_vermelhos_visitante,
        p_escanteios_mandante, p_escanteios_visitante,
        p_impedimentos_mandante, p_impedimentos_visitante,
        p_faltas_mandante, p_faltas_visitante
    ]
    param_names = [
        "id_partida", "gols_mandante", "gols_visitante",
        "cartoes_amarelos_mandante", "cartoes_amarelos_visitante",
        "cartoes_vermelhos_mandante", "cartoes_vermelhos_visitante",
        "escanteios_mandante", "escanteios_visitante",
        "impedimentos_mandante", "impedimentos_visitante",
        "faltas_mandante", "faltas_visitante"
    ]
    
    # Validação: todos os parâmetros devem ser inteiros e não negativos.
    for name, value in zip(param_names, params):
        if not isinstance(value, int):
            raise ValueError(f"O valor para {name} deve ser um inteiro.")
        if value < 0:
            raise ValueError(f"O valor para {name} não pode ser negativo.")
    
    try:
        success = call_sp_encerrar_partida(
            p_id_partida=p_id_partida,
            p_gols_mandante=p_gols_mandante,
            p_gols_visitante=p_gols_visitante,
            p_cartoes_amarelos_mandante=p_cartoes_amarelos_mandante,
            p_cartoes_amarelos_visitante=p_cartoes_amarelos_visitante,
            p_cartoes_vermelhos_mandante=p_cartoes_vermelhos_mandante,
            p_cartoes_vermelhos_visitante=p_cartoes_vermelhos_visitante,
            p_escanteios_mandante=p_escanteios_mandante,
            p_escanteios_visitante=p_escanteios_visitante,
            p_impedimentos_mandante=p_impedimentos_mandante,
            p_impedimentos_visitante=p_impedimentos_visitante,
            p_faltas_mandante=p_faltas_mandante,
            p_faltas_visitante=p_faltas_visitante
        )
        return success
    except Exception as e:
        raise e
